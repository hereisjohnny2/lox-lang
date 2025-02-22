import pprint

from lox.scanner import Scanner


class Lox:
    def run(source: str):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        pprint.pprint(tokens)
