from ast import Expr
from typing import Any

from lox.ast_printer import AstPrinter
from lox.errors import LoxParserError, LoxRunTimeError
from lox.interpreter import Interpreter
from lox.parser import Parser
from lox.scanner import Scanner


class Lox:
    def run(source: str):
        try:
            scanner = Scanner(source)
            tokens = scanner.scan_tokens()

            parser = Parser(tokens)
            expr = parser.parse()

            if not expr:
                return

            interpreter = Interpreter()
            result = interpreter.evaluate(expr)

            print(Lox.stringfy_expression(result))
        except LoxParserError | LoxRunTimeError as e:
            print(e)
            return None

    def stringfy_expression(expr: Any):
        return expr if expr else "nil"
