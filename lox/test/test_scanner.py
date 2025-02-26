import pytest
from lox.scanner import Scanner
from lox.token import Token, TokenType

test_data = [
    ("var", Token(TokenType.VAR, "var", 1)),
    ("and", Token(TokenType.AND, "and", 1)),
    ("class", Token(TokenType.CLASS, "class", 1)),
    ("else", Token(TokenType.ELSE, "else", 1)),
    ("false", Token(TokenType.FALSE, "false", 1)),
    ("fun", Token(TokenType.FUN, "fun", 1)),
    ("for", Token(TokenType.FOR, "for", 1)),
    ("if", Token(TokenType.IF, "if", 1)),
    ("nil", Token(TokenType.NIL, "nil", 1)),
    ("or", Token(TokenType.OR, "or", 1)),
    ("print", Token(TokenType.PRINT, "print", 1)),
    ("return", Token(TokenType.RETURN, "return", 1)),
    ("super", Token(TokenType.SUPER, "super", 1)),
    ("this", Token(TokenType.THIS, "this", 1)),
    ("true", Token(TokenType.TRUE, "true", 1)),
    ("while", Token(TokenType.WHILE, "while", 1)),
    ("str", Token(TokenType.IDENTIFIER, "str", 1)),
    ("=", Token(TokenType.EQUAL, "=", 1)),
    ("==", Token(TokenType.EQUAL_EQUAL, "==", 1)),
    ('"test"', Token(TokenType.STRING, "test", 1, "test")),
    ("1234", Token(TokenType.NUMERIC, "1234", 1, 1234)),
    ("1234.567", Token(TokenType.NUMERIC, "1234.567", 1, 1234.567)),
    (";", Token(TokenType.SEMICOLON, ";", 1)),
    ("(", Token(TokenType.LEFTPAREN, "(", 1)),
    (")", Token(TokenType.RIGHTPARAM, ")", 1)),
    ("{", Token(TokenType.LEFTBRACE, "{", 1)),
    ("}", Token(TokenType.RIGHTBRACE, "}", 1)),
    (",", Token(TokenType.COMMA, ",", 1)),
    (".", Token(TokenType.DOT, ".", 1)),
    ("+", Token(TokenType.PLUS, "+", 1)),
    ("-", Token(TokenType.MINUS, "-", 1)),
    ("*", Token(TokenType.STAR, "*", 1)),
    ("/", Token(TokenType.SLASH, "/", 1)),
    (">", Token(TokenType.GREATER, ">", 1)),
    ("<", Token(TokenType.LESS, "<", 1)),
    ("!", Token(TokenType.BANG, "!", 1)),
    (">=", Token(TokenType.GREATER_EQUAL, ">=", 1)),
    ("<=", Token(TokenType.LESS_EQUAL, "<=", 1)),
    ("!=", Token(TokenType.BANG_EQUAL, "!=", 1)),
]


@pytest.mark.parametrize("source,expected", test_data)
def test_independent_token(source: str, expected: Token):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    assert len(tokens) == 2
    assert tokens[0] == expected
    assert tokens[1] == Token(TokenType.EOF, "", 1)


def test_ignore_comments():
    source = '// var str = "test";'

    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    assert len(tokens) == 1
    assert tokens[0] == Token(TokenType.EOF, "", 1)


def test_scanner_parsing():
    source = 'var str = "test";'

    expected_tokens = [
        Token(TokenType.VAR, "var", 1),
        Token(TokenType.IDENTIFIER, "str", 1),
        Token(TokenType.EQUAL, "=", 1),
        Token(TokenType.STRING, "test", 1, "test"),
        Token(TokenType.SEMICOLON, ";", 1),
        Token(TokenType.EOF, "", 1),
    ]

    scanner = Scanner(source)

    tokens = scanner.scan_tokens()

    assert len(tokens) == 6
    for actual, expected in zip(tokens, expected_tokens):
        assert actual == expected
