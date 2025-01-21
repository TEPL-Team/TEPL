from src.nodes import Set, Output, Binary, Number, Id, Random, Text, If, Condition, Input, While, Repeat, Convert, Pause, Forever, Exit
import random
from typing import Union
import time

def compile_ast(ast):
    compiled_code = ['import random', 'import time', 'INPUT = None']

    if isinstance(ast, list):
        for node in ast:
            compiled_code.append(compile_statements(node))
    else:
        compiled_code.append(compile_statements(ast))

    return '\n'.join(compiled_code)

def compile_statements(stmt, indent_level=0):
    if isinstance(stmt, list):
        return '\n'.join([compile_statements(s, indent_level) for s in stmt])

    method_name = f'compile_{type(stmt).__name__.lower()}'
    method = globals().get(method_name)
    if method:
        return method(stmt, indent_level)
    else:
        raise TypeError(f"Unknown statement type: {type(stmt).__name__}")

def compile_output(node, indent_level=0):
    expr_code = compile_expr(node.value)
    indent = '    ' * indent_level
    return f"{indent}print({expr_code})"

def compile_set(node, indent_level=0):
    value = compile_expr(node.value)
    name = node.name.name  # Ensure name is extracted from Id
    indent = '    ' * indent_level
    return f"{indent}{name} = {value}"

def compile_if(node, indent_level=0):
    condition = compile_expr(node.condition)
    statements = compile_statements(node.body, indent_level + 1)  # Increase indent level for block
    indented_statements = '\n'.join(['    ' * indent_level + line for line in statements.split('\n')])
    indent = '    ' * indent_level
    return f"{indent}if {condition}:\n{indented_statements}"

def compile_while(node, indent_level=0):
    condition = compile_expr(node.cond)
    statements = compile_statements(node.body, indent_level + 1)  # Increase indent level for block
    indented_statements = '\n'.join(['    ' * indent_level + line for line in statements.split('\n')])
    indent = '    ' * indent_level
    return f"{indent}while {condition}:\n{indented_statements}"

def compile_input(node, indent_level=0):
    indent = '    ' * indent_level
    return f"{indent}INPUT = input({compile_expr(node.question)})"

def compile_pause(node, indent_level=0):
    indent = '    ' * indent_level
    return f"{indent}time.sleep({compile_expr(node.duration)})"

def compile_forever(node, indent_level=0):
    statements = compile_statements(node.body, indent_level + 1)  # Increase indent level for block
    indented_statements = '\n'.join(['    ' * indent_level + line for line in statements.split('\n')])
    indent = '    ' * indent_level
    return f"{indent}while True:\n{indented_statements}"

def compile_exit(node, indent_level=0):
    indent = '    ' * indent_level
    return f"{indent}break"

def compile_repeat(node, indent_level=0):
    times = compile_expr(node.times)
    loop_var = node.id.name  # Ensure name is extracted from Id
    statements = compile_statements(node.body, indent_level + 1)  # Increase indent level for block
    indented_statements = '\n'.join(['    ' * indent_level + line for line in statements.split('\n')])
    indent = '    ' * indent_level
    return f"{indent}for {loop_var} in range({times}):\n{indented_statements}"

def compile_expr(expr):
    if isinstance(expr, list):
        return ', '.join([compile_expr(e) for e in expr])

    elif isinstance(expr, (Number, Text)):
        return str(expr.value)

    elif isinstance(expr, Id):
        return expr.name

    elif isinstance(expr, Binary):
        left_code = compile_expr(expr.left)
        right_code = compile_expr(expr.right)
        return f"{left_code} {expr.op} {right_code}"

    elif isinstance(expr, Random):
        low = compile_expr(expr.low)
        max = compile_expr(expr.max)
        if expr.type == 'number':
            return f"random.randint({low}, {max})"
        else:
            raise TypeError(f"Unsupported type: {expr.type} for 'random'")
        
    elif isinstance(expr, Convert):
        value = compile_expr(expr.value)
        if expr.to.upper() == 'NUM':
            return f"int({value})"
        elif expr.to.upper() == 'TXT':
            return f"str({value})"
        else:
            raise TypeError(f"Unsupported type: {expr.to} for 'convert'")
        
    elif isinstance(expr, Condition):
        left_code = compile_expr(expr.left)
        right_code = compile_expr(expr.right)
        return f"{left_code} {expr.op} {right_code}"

    else:
        raise TypeError(f"Unknown expression type: {type(expr).__name__}")

