import enum
from typing import Any


class TokenType(enum.Enum):
    VAR = 0
    IDENTIFIER = 1
    EQUAL = 2
    STRING = 3
    SEMICOLON = 4
    EOF = 5


KEYWORDS = {
    "var": TokenType.VAR,
}


class Token:
    def __init__(
        self,
        type: TokenType,
        lexeme: str,
        line: int,
        literal: Any | None = None,
    ):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        out = f"[{self.type}, '{self.lexeme}'"
        if self.literal:
            out += f", '{self.literal}'"

        return out + "]"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, value: "Token"):
        return (
            self.lexeme == value.lexeme
            and self.type == value.type
            and self.literal == value.literal
            and self.line == value.line
        )
