from lox.ast_printer import AstPrinter
from lox.expr_ast import Binary, Grouping, Literal, Unary
from lox.token import Token, TokenType


def test_print_ast():
    expected = "(* (- 123) (group 45.67))"
    unary_expr1 = Unary(Token(TokenType.MINUS, "-", 1), Literal(123))
    operator = Token(TokenType.STAR, "*", 1)
    unary_expr2 = Grouping(Literal(45.67))

    expr = Binary(unary_expr1, operator, unary_expr2)

    actual = AstPrinter().print(expr)

    assert expected == actual
