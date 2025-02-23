import pytest
from lox.scanner import Scanner
from lox.token import Token, TokenType

test_data = [
    ("var", Token(TokenType.VAR, "var", 1)),
    ("str", Token(TokenType.IDENTIFIER, "str", 1)),
    ("=", Token(TokenType.EQUAL, "=", 1)),
    ('"test"', Token(TokenType.STRING, "test", 1, "test")),
    ("1234", Token(TokenType.NUMERIC, "1234", 1, 1234)),
    ("1234.567", Token(TokenType.NUMERIC, "1234.567", 1, 1234.567)),
    (";", Token(TokenType.SEMICOLON, ";", 1)),
]


@pytest.mark.parametrize("source,expected", test_data)
def test_independent_token(source: str, expected: Token):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    assert len(tokens) == 2
    assert tokens[0] == expected
    assert tokens[1] == Token(TokenType.EOF, "", 1)


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
