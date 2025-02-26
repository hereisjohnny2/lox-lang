from pathlib import Path
import sys


def define_ast(output_path: Path, base_name: str, types: dict[str, str]):
    filepath = output_path / f"{base_name}_ast.py"
    with filepath.open("w") as f:
        lines = [
            "# Auto generate AST file from tools/ast_generator.py\n\n",
            "from abc import ABC, abstractmethod\n",
            "from lox.token import Token\n\n",
            "from typing import Any\n\n",
            f"class {base_name.title()}(ABC):\n",
            "\t@abstractmethod\n",
            '\tdef accept(visitor: "Visitor"): ...',
            "\n\n\n",
        ]

        lines.extend(define_visitor(base_name, types))

        lines.extend(
            [define_type(base_name, type, fields) for type, fields in types.items()]
        )

        f.writelines(lines)

    return filepath


def define_type(base_name: str, type: str, fields: str):
    return (
        f"class {type}({base_name.title()}):\n"
        + f"\tdef __init__(self, {fields.strip()}):\n"
        + "".join([define_field(field) for field in fields.split(",")])
        + "\n"
        + '\tdef accept(self, visitor: "Visitor"):\n'
        + f"\t\treturn visitor.visit_{type.lower()}_{base_name}(self)\n"
        + "\n\n"
    )


def define_field(field: str):
    field_name = field.strip().split(":")[0]
    return f"\t\tself.{field_name} = {field_name}\n"


def define_visitor(base_name: str, types: dict[str, str]):
    lines = ["class Visitor(ABC):\n"]

    for type in types.keys():
        lines.append("\t@abstractmethod\n")
        lines.append(f'\tdef visit_{type.lower()}_{base_name}(expr: "{type}"): ...\n\n')

    lines.append("\n")

    return lines


def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 ast_generator.py <path/to/output_ast_dir>")
        exit(1)

    output_path = Path(args[1])
    types = {
        "Binary": "left: Expr, operator: Token, right: Expr",
        "Grouping": "expression: Expr",
        "Literal": "value: Any",
        "Unary": "operator: Token, right: Expr",
    }

    filepath = define_ast(output_path, "expr", types)
    print("AST generated at", filepath.absolute())


if __name__ == "__main__":
    main()
