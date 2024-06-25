from parser import parser
from parser import __error__
from nodes import *


def transpile(ast):
    compiled_code = ['import random', 'import time', 'INPUT = None']

    def transpile_node(node):
        if isinstance(node, BinOp):
            left = transpile_node(node.left)
            right = transpile_node(node.right)
            return f"({left} {node.op} {right})"

        elif isinstance(node, Number):
            return str(node.value)

        elif isinstance(node, Boolean):
            return 'True' if node.value.upper() == 'YES' else 'False'

        elif isinstance(node, Identifier):
            return node.name

        elif isinstance(node, Output):
            return f"print({transpile_node(node.expr)})"

        elif isinstance(node, Assignment):
            if node.value is None:
                return f"{node.name.name} = None"
            else:
                return f"{node.name.name} = {transpile_node(node.value)}"

        elif isinstance(node, Random):
            return f"random.randint({transpile_node(node._from)}, {transpile_node(node.to)})"

        elif isinstance(node, Input):
            return f"INPUT"

        elif isinstance(node, Comparism):
            left = transpile_node(node.left) if node.left else ''
            right = transpile_node(node.right)
            return f"({left} {node.op} {right})"

        elif isinstance(node, If):
            condition = transpile_node(node.condition)
            body = '\n'.join([transpile_node(stmt) for stmt in node.body])
            body = body.replace('\n', )
            if_body = f"if {condition}:\n    {body.replace('\n', ' ')}"
            if node.conelse:
                else_body = '\n'.join(
                    [transpile_node(stmt) for stmt in node.elsebody])
                if_body += f"\nelse:\n    {else_body.replace('\n', '\\n    ')}"
            return if_body

        elif isinstance(node, EndStatement):
            return ''

        elif isinstance(node, Text):
            return node.text

        elif isinstance(node, Repeat):
            condition = transpile_node(node.condition)
            body = '\n'.join([transpile_node(stmt) for stmt in node.body])
            return f"while not ({condition}):\n    {body.replace('\n', '\\n    ')}"

        elif isinstance(node, Pause):
            return f"time.sleep({transpile_node(node.time)})"

        elif isinstance(node, Type):
            return ''  # Placeholder if needed for variable type annotations

        elif isinstance(node, Function):
            args = ', '.join(node.args) if node.args else ''
            body = '\n'.join([transpile_node(stmt) for stmt in node.body])
            return f"def {node.name.name}({args}):\n    {body.replace('\n', '\\n    ')}"

        elif isinstance(node, While):
            condition = transpile_node(node.condition)
            body = '\n'.join([transpile_node(stmt) for stmt in node.body])
            return f"while {condition}:\n    {body.replace('\n', '\\n    ')}"

        elif isinstance(node, Forever):
            body = '\n'.join([transpile_node(stmt) for stmt in node.body])
            return f"while True:\n    {body.replace('\n', '\\n    ')}"

        elif isinstance(node, Exit):
            return "break"

        elif isinstance(node, Substring):
            return f"{transpile_node(node.string)}[{transpile_node(node.from_expr)}:{transpile_node(node.to_expr)}]"

        elif isinstance(node, Length):
            return f"len({transpile_node(node.expr)})"

        elif isinstance(node, Find):
            return f"{transpile_node(node.string)}.count({transpile_node(node.char)})"

        elif isinstance(node, Convert):
            to_type = node.to_type.lower()
            expr = transpile_node(node.expr)
            if to_type == 'num':
                return f"int({expr})"
            elif to_type == 'dec':
                return f"float({expr})"
            elif to_type == 'txt':
                return f"str({expr})"

        elif isinstance(node, Call):
            args = ', '.join([transpile_node(arg)
                              for arg in node.args]) if node.args else ''
            return f"{node.name.name}({args})"

        elif isinstance(node, Return):
            return f"return {transpile_node(node.expr)}"

        elif isinstance(node, Delete):
            if node.index is None:
                return f"del {node.name.name}"
            else:
                return f"del {node.name.name}[{transpile_node(node.index)}]"

        elif isinstance(node, Index):
            return f"{node.name.name}[{transpile_node(node.index)}]"

        elif isinstance(node, Clear):
            return f"{node._list.name}.clear()"

        elif isinstance(node, For):
            body = '\n'.join([transpile_node(stmt) for stmt in node.body])
            return f"for {node.name.name} in range({transpile_node(node.times)}):\n    {body.replace('\n', '\\n    ')}"

    compiled_code += [transpile_node(statement) for statement in ast]
    return '\n'.join(compiled_code)
