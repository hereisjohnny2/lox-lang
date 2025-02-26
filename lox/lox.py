import pprint

from lox.ast_printer import AstPrinter
from lox.parser import Parser
from lox.scanner import Scanner


class Lox:
    def run(source: str):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        pprint.pprint(tokens)

        parser = Parser(tokens)
        expr = parser.parse()

        if not expr:
            return

        ast_printer = AstPrinter()
        print(ast_printer.print(expr))
