"""
Tests to ensure our code works nicely with Flask
"""
import pytest
import pyhtml as p
from flask import Flask
from flask.testing import FlaskClient


app = Flask(__name__)


@app.get("/")
def simple_route():
    return str(p.html(
        p.body("Hello, world!")
    ))


# This route intentionally returns the wrong type
@app.get("/no_str")  # type: ignore
def no_stringify():
    """
    This route intentionally returns an un-stringified PyHTML object. We use
    it to test that a reasonable error message is given
    """
    return p.html(
        p.body("Hello, world!")
    )


@pytest.fixture
def get_app():
    app.config.update({"TESTING": True})

    yield app

    app.config.pop("TESTING")


@pytest.fixture
def client(get_app: Flask):
    return get_app.test_client()


def test_simple_stringify(client: FlaskClient):
    """Does requesting to the server give some nice HTML?"""
    response = client.get("/")
    assert response.status_code == 200

    assert response.text == '\n'.join([
        "<html>",
        "  <body>",
        "    Hello, world!",
        "  </body>",
        "</html>",
    ])


def test_failed_to_stringify(client: FlaskClient):
    """
    Does requesting to a route that returns un-stringified HTML give an
    appropriate error message
    """
    with pytest.raises(TypeError) as exception_info:
        client.get("/no_str")

    expected_error = "HINT: try converting your PyHTML into a string using "\
        "the `str` function"

    assert expected_error in str(exception_info.value)
