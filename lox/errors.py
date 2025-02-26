from lox.token import Token, TokenType


class LoxParserError(Exception):
    def __init__(self, token: Token, msg: str):
        if token.type == TokenType.EOF:
            super().__init__("Lox Error:", token.line, " at end", msg)
        else:
            super().__init__("Lox Error:", token.line, " at '", token.lexeme, "'", msg)
