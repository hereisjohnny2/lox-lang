from lox.parser import Parser
from lox.token import Token, TokenType


def test_parse_expression():
    tokens = [
        Token(TokenType.NUMERIC, "1", 1, 1),
        Token(TokenType.PLUS, "+", 1),
        Token(TokenType.NUMERIC, "2", 1, 2),
        Token(TokenType.EOF, "", 1),
    ]

    parser = Parser(tokens)
    actual_expr = parser.parse()

    assert actual_expr
