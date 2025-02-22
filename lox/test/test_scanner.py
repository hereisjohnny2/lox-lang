from lox.scanner import Scanner
from lox.token import Token, TokenType


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
