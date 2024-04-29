from parser import parser
from parser import __error__
from nodes import *


def transpile(ast):
    compiled_code = []
    compiled_code.append('import random')
    compiled_code.append('import time')
    compiled_code.append('INPUT = None')

    if isinstance(ast, list):
        for node in ast:
            if isinstance(node, Output):
                compiled_code.append(compile_output(node))
            elif isinstance(node, If):
                compiled_code.append(compile_if(node))
            elif isinstance(node, Assignment):
                compiled_code.append(compile_assignment(node))
            elif isinstance(node, Repeat):
                compiled_code.append(compile_repeat(node))

            elif isinstance(node, Pause):
                compiled_code.append(compile_pause(node))

    else:
        if isinstance(ast, Output):
            compiled_code.append(compile_output(ast))
        elif isinstance(ast, If):
            compiled_code.append(compile_if(ast))
        elif isinstance(ast, Assignment):
            compiled_code.append(compile_assignment(ast))
        elif isinstance(ast, Repeat):
            compiled_code.append(compile_repeat(ast))
        elif isinstance(ast, Pause):
            compiled_code.append(compile_pause(ast))
        else:
            raise TypeError(
                "Invalid AST root node. Expecting an 'Output' node or list of statements, but got "
                + str(type(ast)))

    return '\n'.join(compiled_code)


def transpile_stmt(stmt, ident_level=0):
    if isinstance(stmt, list):
        return ('\n').join([transpile_stmt(s, ident_level) for s in stmt])

    if isinstance(stmt, Output):
        return compile_output(stmt, ident_level)

    elif isinstance(stmt, If):
        return compile_if(stmt, ident_level)

    elif isinstance(stmt, Assignment):
        return compile_assignment(stmt, ident_level)

    elif isinstance(stmt, Repeat):
        return compile_repeat(stmt, ident_level)

    elif isinstance(stmt, Pause):
        return compile_pause(stmt, ident_level)


def compile_output(stmt, indent_level=0):
    expr_code = compile_expr(stmt.expr)
    if str(expr_code).startswith('input('):
        return f"{'    ' * indent_level}INPUT = {expr_code}\n{'    ' * indent_level}print(INPUT)"
    else:
        return f"{'    ' * indent_level}print({expr_code})"


def compile_assignment(stmt, indent_level=0):
    name = compile_expr(stmt.name)
    value = compile_expr(stmt.value)
    return f"{'    ' * indent_level}{name} = {value}"


def compile_if(stmt, indent_level=0):
    comp = compile_expr(stmt.condition)
    body = transpile_stmt(stmt.body, indent_level + 1)
    elsed = stmt.conelse

    if elsed:
        else_body = transpile_stmt(stmt.elsebody, indent_level + 1)
        return f"{'    ' * indent_level}if {comp}:\n{body}\n{'    ' * indent_level}else:\n{else_body}"
    else:
        return f"{'    ' * indent_level}if {comp}:\n{body}"


def compile_repeat(stmt, indent_level=0):
    comp = compile_expr(stmt.condition)
    body = transpile_stmt(stmt.body, indent_level + 1)
    some = indent_level + 2
    some2 = some - 1
    return f"{'    ' * indent_level}while True:\n{body}\n{'    ' * some2}if {comp}:\n{'    ' * some}    break"


def compile_pause(stmt, indent_level=0):
    return f"{'    ' * indent_level}time.sleep({compile_expr(stmt.time)})"


def compile_expr(expr):
    if isinstance(expr, list):
        # If the expression is a list, compile each element in the list
        return ', '.join([compile_expr(e) for e in expr])
    elif isinstance(expr, Number):
        return int(expr.value)
    elif isinstance(expr, BinOp):
        left_code = compile_expr(expr.left)
        right_code = compile_expr(expr.right)
        return f"{left_code} {expr.op} {right_code}"
    elif isinstance(expr, Identifier):
        return f"{expr.name}"
    elif isinstance(expr, Boolean):
        return 'True' if expr.value.lower() == 'YES' else 'False'
    elif isinstance(expr, Text):
        return f"{str(expr.text)}"
    elif isinstance(expr, Input):
        if expr.t.upper() == 'NUM':
            return f"int(input({expr.q}))"
        elif expr.t.upper() == 'DEC':
            pass
        elif expr.t.upper() == 'TXT':
            return f"input({expr.q})"
        elif expr.t.upper() == 'BOOL':
            return f"bool(input({expr.q}))"
        else:
            return print(
                f"TypeError: {expr.t} is not a valid data type, only NUM, TXT, and BOOL are valid!"
            )
    elif isinstance(expr, Random):
        return f"random.randint({expr._from.value}, {expr.to.value})"
    elif isinstance(expr, Input_Expr):
        return 'INPUT'
    elif isinstance(expr, Comparism):
        if expr.left is None:
            left = compile_expr(expr.left)
            right = compile_expr(expr.right)
            if expr.op in ['>', '<', '>=', '<=', '==', '!=']:
                return print(
                    f"Error: {expr.op} is not a valid operator in expression, {expr}!"
                )
            else:
                match expr.op:
                    case 'AND':
                        return f"({left} and {right})"
                    case 'OR':
                        return f"({left} or {right})"
                    case 'NOT':
                        return f"not {right}"
                    case 'IN':
                        return f"({left} in {right})"
                    case _:
                        return print(
                            f"Error: {expr.op} is not a valid operator in expression, {expr}!"
                        )
        else:
            left_code = compile_expr(expr.left)
            right_code = compile_expr(expr.right)
            return f"{left_code} {expr.op} {right_code}"
    else:
        raise TypeError(f"Unknown expression type: {expr}")
