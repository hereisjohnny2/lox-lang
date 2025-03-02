from typing import Any
from lox.errors import LoxRunTimeError
from lox.token import Token, TokenType
from lox.expr_ast import Binary, Expr, Grouping, Literal, Unary, Visitor


class Interpreter(Visitor):
    def visit_binary_expr(self, expr: Binary):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        match expr.operator.type:
            case TokenType.PLUS:
                if self.is_numeric(left, right):
                    return float(left) + float(right)
                if self.is_str(left, right):
                    return str(left) + str(right)
                raise LoxRunTimeError(
                    expr.operator, "Operands must be two numbers or two strings"
                )
            case TokenType.MINUS:
                self.check_number_operands(expr.operator, left, right)
                return float(left) - float(right)
            case TokenType.STAR:
                self.check_number_operands(expr.operator, left, right)
                return float(left) * float(right)
            case TokenType.SLASH:
                self.check_number_operands(expr.operator, left, right)
                return float(left) / float(right)
            case TokenType.GREATER:
                self.check_number_operands(expr.operator, left, right)
                return float(left) > float(right)
            case TokenType.GREATER_EQUAL:
                self.check_number_operands(expr.operator, left, right)
                return float(left) >= float(right)
            case TokenType.LESS:
                self.check_number_operands(expr.operator, left, right)
                return float(left) < float(right)
            case TokenType.LESS_EQUAL:
                self.check_number_operands(expr.operator, left, right)
                return float(left) <= float(right)
            case TokenType.EQUAL_EQUAL:
                return left == right
            case TokenType.BANG_EQUAL:
                return left != right

        return None

    def is_str(self, left, right):
        return isinstance(left, str) and isinstance(right, str)

    def is_numeric(self, left, right):
        return (isinstance(left, float) or isinstance(left, int)) and (
            isinstance(right, float) or isinstance(right, int)
        )

    def visit_grouping_expr(self, expr: Grouping):
        return self.evaluate(expr.expression)

    def visit_literal_expr(self, expr: Literal):
        return expr.value

    def visit_unary_expr(self, expr: Unary):
        right = self.evaluate(expr.right)

        match expr.operator.type:
            case TokenType.BANG:
                return not self.is_truthy(right)
            case TokenType.MINUS:
                self.check_number_operands(expr.operator, right)
                return -float(right)

        return None

    def check_number_operands(self, operator: Token, *operands: Any):
        if all(isinstance(op, float) or isinstance(op, int) for op in operands):
            return

        raise LoxRunTimeError(operator, "All operands must be a number")

    def evaluate(self, expr: Expr) -> Expr:
        return expr.accept(self)

    def is_truthy(self, expr: Any):
        if not expr:
            return None
        if isinstance(type(expr), bool):
            return expr

        return True
