from pathlib import Path
import sys
from lox.lox import Lox


def run_script(filepath: Path):
    with filepath.open() as f:
        source = f.read()

    Lox.run(source)


def run_prompt():
    print("Lox Lang - v0.1")
    while True:
        line = input("> ")
        Lox.run(line)


def main():
    args = sys.argv
    if len(args) < 3 and "-h" in args:
        print("Usage: python3 main.py [path_to_script]")
        exit(0)
    if len(args) == 1:
        run_prompt()
    elif len(args) == 2:
        run_script(Path(args[1]))
    else:
        print("Usage: python3 main.py [path_to_script]")
        exit(1)


if __name__ == "__main__":
    main()
