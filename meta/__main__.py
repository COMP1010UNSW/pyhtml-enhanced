from pathlib import Path

from . import build_tags

OUTPUT_FILE = Path("pyhtml/__tags/generated.py")


def main():
    with open(OUTPUT_FILE, "w") as f:
        build_tags(f)


if __name__ == "__main__":
    main()
