from io import StringIO
from pathlib import Path

from . import build_tags

GENERATED_OUT = Path("pyhtml/__tags/generated.py")
TAGS_INIT_OUT = Path("pyhtml/__tags/__init__.py")
PYHTML_INIT_OUT = Path("pyhtml/__init__.py")


def main():
    generated = StringIO()
    tags_init = StringIO()
    pyhtml_init = StringIO()
    build_tags(generated, tags_init, pyhtml_init)
    generated.seek(0)
    tags_init.seek(0)
    pyhtml_init.seek(0)
    with open(GENERATED_OUT, "w") as f:
        f.write(generated.read())
    with open(TAGS_INIT_OUT, "w") as f:
        f.write(tags_init.read())
    with open(PYHTML_INIT_OUT, "w") as f:
        f.write(pyhtml_init.read())


if __name__ == "__main__":
    main()
