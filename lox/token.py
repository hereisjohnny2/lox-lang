import enum
from typing import Any


class TokenType(enum.Enum):
    # Keywords
    VAR = enum.auto()
    AND = enum.auto()
    CLASS = enum.auto()
    ELSE = enum.auto()
    FALSE = enum.auto()
    FUN = enum.auto()
    FOR = enum.auto()
    IF = enum.auto()
    NIL = enum.auto()
    OR = enum.auto()
    PRINT = enum.auto()
    RETURN = enum.auto()
    SUPER = enum.auto()
    THIS = enum.auto()
    TRUE = enum.auto()
    WHILE = enum.auto()
    # Literals
    IDENTIFIER = enum.auto()
    STRING = enum.auto()
    NUMERIC = enum.auto()
    # Single Characters Tokens
    SEMICOLON = enum.auto()
    LEFTPARAM = enum.auto()
    RIGHTPARAM = enum.auto()
    LEFTBRACE = enum.auto()
    RIGHTBRACE = enum.auto()
    COMMA = enum.auto()
    DOT = enum.auto()
    PLUS = enum.auto()
    MINUS = enum.auto()
    STAR = enum.auto()
    SLASH = enum.auto()
    # One or Two Characters Tokens
    EQUAL = enum.auto()
    EQUAL_EQUAL = enum.auto()
    GREATER = enum.auto()
    GREATER_EQUAL = enum.auto()
    LESS = enum.auto()
    LESS_EQUAL = enum.auto()
    BANG = enum.auto()
    BANG_EQUAL = enum.auto()
    EOF = enum.auto()


KEYWORDS = {
    "var": TokenType.VAR,
    "and": TokenType.AND,
    "class": TokenType.CLASS,
    "else": TokenType.ELSE,
    "false": TokenType.FALSE,
    "fun": TokenType.FUN,
    "for": TokenType.FOR,
    "if": TokenType.IF,
    "nil": TokenType.NIL,
    "or": TokenType.OR,
    "print": TokenType.PRINT,
    "return": TokenType.RETURN,
    "super": TokenType.SUPER,
    "this": TokenType.THIS,
    "true": TokenType.TRUE,
    "while": TokenType.WHILE,
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
