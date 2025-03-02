# Auto generate AST file from tools/ast_generator.py

from abc import ABC, abstractmethod
from lox.token import Token

from typing import Any

class Expr(ABC):
	@abstractmethod
	def accept(visitor: "Visitor"): ...


class Visitor(ABC):
	@abstractmethod
	def visit_binary_expr(expr: "Binary"): ...

	@abstractmethod
	def visit_grouping_expr(expr: "Grouping"): ...

	@abstractmethod
	def visit_literal_expr(expr: "Literal"): ...

	@abstractmethod
	def visit_unary_expr(expr: "Unary"): ...


class Binary(Expr):
	def __init__(self, left: Expr, operator: Token, right: Expr):
		self.left = left
		self.operator = operator
		self.right = right

	def accept(self, visitor: "Visitor"):
		return visitor.visit_binary_expr(self)


class Grouping(Expr):
	def __init__(self, expression: Expr):
		self.expression = expression

	def accept(self, visitor: "Visitor"):
		return visitor.visit_grouping_expr(self)


class Literal(Expr):
	def __init__(self, value: Any):
		self.value = value

	def accept(self, visitor: "Visitor"):
		return visitor.visit_literal_expr(self)


class Unary(Expr):
	def __init__(self, operator: Token, right: Expr):
		self.operator = operator
		self.right = right

	def accept(self, visitor: "Visitor"):
		return visitor.visit_unary_expr(self)


