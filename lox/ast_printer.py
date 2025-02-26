from lox import expr_ast


class AstPrinter(expr_ast.Visitor):
    def print(self, expr: expr_ast.Expr):
        return expr.accept(self)

    def visit_binary_expr(self, expr: expr_ast.Binary):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visit_grouping_expr(self, expr: expr_ast.Grouping):
        return self.parenthesize("group", expr.expression)

    def visit_literal_expr(self, expr: expr_ast.Literal):
        return expr.value if expr.value else "nil"

    def visit_unary_expr(self, expr: expr_ast.Unary):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name: str, *args: expr_ast.Expr):
        return f"({name}" + "".join(f" {str(expr.accept(self))}" for expr in args) + ")"
