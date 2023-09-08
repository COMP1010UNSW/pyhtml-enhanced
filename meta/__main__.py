
from pathlib import Path
from . import build_tags


OUTPUT_FILE = Path("pyhtml/__tags/generated.py")


def main():
    build_tags(open(OUTPUT_FILE, "w"))


if __name__ == '__main__':
    main()
