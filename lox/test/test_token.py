from lox.token import Token, TokenType


def test_create_token():
    token = Token(TokenType.STRING, "test", 1)
    assert str(token) == "[TokenType.STRING, 'test']"
