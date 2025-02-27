import pytest
from lox.errors import LoxRunTimeError
from lox.expr_ast import Binary, Grouping, Literal, Unary
from lox.interpreter import Interpreter
from lox.token import Token, TokenType

bool_ops = [
    (Token(TokenType.GREATER, ">", 1), True),
    (Token(TokenType.GREATER_EQUAL, ">=", 1), True),
    (Token(TokenType.LESS, "<", 1), False),
    (Token(TokenType.LESS_EQUAL, "<=", 1), False),
    (Token(TokenType.EQUAL_EQUAL, "==", 1), True),
    (Token(TokenType.BANG_EQUAL, "!=", 1), False),
]


@pytest.mark.parametrize("op,expected", bool_ops)
def test_evaluate_bool_expression(op: Token, expected: bool):
    expr = Unary(
        Token(TokenType.BANG, "!", 1),
        Binary(Literal(1), op, Literal(2)),
    )

    assert_expr(expr, expected)


def test_evaluate_str_expression():
    expr = Binary(
        Literal("MiuMiu "),
        Token(TokenType.PLUS, "+", 1),
        Binary(
            Literal("e Tudinha "),
            Token(TokenType.PLUS, "+", 1),
            Literal("e Jujubinha"),
        ),
    )

    expected = "MiuMiu e Tudinha e Jujubinha"
    assert_expr(expr, expected)


def test_evaluate_numeric_expression():
    # expr = 1 + 3 / 3 * (5.2 - 9) = 2
    expr = Unary(
        Token(TokenType.MINUS, "-", 1),
        Binary(
            Literal(1),
            Token(TokenType.PLUS, "+", 1),
            Binary(
                Binary(
                    Literal(3),
                    Token(TokenType.SLASH, "/", 1),
                    Literal(3),
                ),
                Token(TokenType.STAR, "*", 1),
                Grouping(
                    Binary(
                        Literal(5.2),
                        Token(TokenType.MINUS, "-", 1),
                        Literal(9),
                    )
                ),
            ),
        ),
    )

    expected = 2.8
    assert_expr(expr, expected)


binary_numeric_ops = [
    (Token(TokenType.GREATER, ">", 1)),
    (Token(TokenType.GREATER_EQUAL, ">=", 1)),
    (Token(TokenType.LESS, "<", 1)),
    (Token(TokenType.LESS_EQUAL, "<=", 1)),
    (Token(TokenType.MINUS, "-", 1)),
    (Token(TokenType.STAR, "*", 1)),
    (Token(TokenType.SLASH, "/", 1)),
]


@pytest.mark.parametrize("op", binary_numeric_ops)
def test_raise_when_binary_op_invalid_operand(op: Token):
    expr = Binary(Literal(1), op, Literal("Invalid"))

    with pytest.raises(LoxRunTimeError) as error:
        assert_expr(expr, None)

    assert (
        error.value.args[0]
        == f"[Lox Error] Line {op.line} at '{op.lexeme}': All operands must be a number."
    )
    assert error.value.operator == op


def test_raise_when_plus_op_invalid_operand():
    expr = Binary(
        Literal(1),
        Token(TokenType.PLUS, "+", 1),
        Literal("Invalid"),
    )

    with pytest.raises(LoxRunTimeError) as error:
        assert_expr(expr, None)

    assert (
        error.value.args[0]
        == "[Lox Error] Line 1 at '+': Operands must be two numbers or two strings."
    )
    assert error.value.operator == Token(TokenType.PLUS, "+", 1)


def test_raise_when_invalid_operand():
    expr = Unary(Token(TokenType.MINUS, "-", 1), Literal("Invalid"))

    with pytest.raises(LoxRunTimeError) as error:
        assert_expr(expr, None)

    assert (
        error.value.args[0]
        == "[Lox Error] Line 1 at '-': All operands must be a number."
    )
    assert error.value.operator == Token(TokenType.MINUS, "-", 1)


def assert_expr(expr, expected):
    interpreter = Interpreter()
    actual = interpreter.evaluate(expr)

    assert actual == expected
