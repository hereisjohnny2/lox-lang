from lox.token import Token, TokenType


class LoxParserError(Exception):
    def __init__(self, token: Token, msg: str):
        self.token = token

        if token.type == TokenType.EOF:
            super().__init__(f"[Lox Error] Line {token.line} at end: {msg}.")
        else:
            super().__init__(
                f"[Lox Error] Line {token.line} at '{token.lexeme}': {msg}."
            )


class LoxRunTimeError(Exception):
    def __init__(self, operator: Token, msg: str):
        self.operator = operator
        super().__init__(
            f"[Lox Error] Line {operator.line} at '{operator.lexeme}': {msg}."
        )
