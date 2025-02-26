from ast import Expr
from lox.errors import LoxParserError
from lox.expr_ast import Binary, Grouping, Literal, Unary
from lox.token import Token, TokenType


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        try:
            return self.expression()
        except LoxParserError as e:
            print(e)
            return None

    def expression(self) -> Expr:
        return self.equality()

    def equality(self) -> Expr:
        expr = self.comparison()

        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)

        return expr

    def comparison(self) -> Expr:
        expr = self.term()

        while self.match(
            TokenType.LESS,
            TokenType.LESS_EQUAL,
            TokenType.GREATER,
            TokenType.GREATER_EQUAL,
        ):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)

        return expr

    def term(self) -> Expr:
        expr = self.factor()

        while self.match(TokenType.PLUS, TokenType.MINUS):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)

        return expr

    def factor(self) -> Expr:
        expr = self.unary()

        while self.match(TokenType.STAR, TokenType.SLASH):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)

        return expr

    def unary(self) -> Expr:
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)

        return self.primary()

    def primary(self) -> Expr:
        if self.match(TokenType.FALSE):
            return Literal(False)
        if self.match(TokenType.TRUE):
            return Literal(True)
        if self.match(TokenType.NIL):
            return Literal(None)
        if self.match(TokenType.NUMERIC, TokenType.STRING):
            return Literal(self.previous().literal)

        if self.match(TokenType.LEFTPAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHTPARAM, "expected ')' after expression.")
            return Grouping(expr)

        raise LoxParserError(self.peek(), "expected expression")

    def match(self, *args: TokenType) -> bool:
        for type in args:
            if self.check(type):
                self.advance()
                return True

        return False

    def check(self, type: TokenType) -> bool:
        if self.at_end():
            return False

        return self.peek().type == type

    def advance(self) -> Token:
        if not self.at_end():
            self.current += 1

        return self.previous()

    def at_end(self) -> bool:
        return self.peek().type == TokenType.EOF

    def peek(self) -> Token:
        return self.tokens[self.current]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    def consume(self, type: TokenType, msg: str) -> Token:
        if self.check(type):
            return self.advance()

        raise LoxParserError(self.peek(), msg)

    def synchronize(self):
        self.advance()
        while not self.at_end():
            if self.previous().type == TokenType.SEMICOLON:
                return

            match self.peek().type:
                case (
                    TokenType.CLASS
                    | TokenType.FUN
                    | TokenType.VAR
                    | TokenType.FOR
                    | TokenType.IF
                    | TokenType.WHILE
                    | TokenType.PRINT
                    | TokenType.RETURN
                ):
                    return

            self.advance()
