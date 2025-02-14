"""
# tests / custom tag test

Test cases for generating custom tags.
"""
import pyhtml as p


def test_generate_custom_tag():
    t = p.create_tag('t')

    assert str(t()) == '<t></t>'


def test_base_class_set():
    t = p.create_tag('t', p.SelfClosingTag)

    assert issubclass(t, p.SelfClosingTag)
