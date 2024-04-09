from parser import parser
from parser import __error__
from nodes import *


def transpile(ast):
    compiled_code = []
    compiled_code.append('import random')
    compiled_code.append('INPUT = None')

    if isinstance(ast, list):
        for node in ast:
            if isinstance(node, Output):
                compiled_code.append(compile_output(node))
            elif isinstance(node, If):
                compiled_code.append(compile_if(node))
            elif isinstance(node, Assignment):
                compiled_code.append(compile_assignment(node))

    else:
        if isinstance(ast, Output):
            compiled_code.append(compile_output(ast))
        elif isinstance(ast, If):
            compiled_code.append(compile_if(ast))
        elif isinstance(ast, Assignment):
            compiled_code.append(compile_assignment(ast))
        else:
            raise TypeError(
                "Invalid AST root node. Expecting an 'Output' node or list of statements, but got "+str(type(ast))
            )

    return '\n'.join(compiled_code)


def transpile_stmt(stmt):
    if isinstance(stmt, list):
        return '\n'.join([transpile_stmt(s) for s in stmt])
    if isinstance(stmt, Output):
        return compile_output(stmt)

    elif isinstance(stmt, If):
        return compile_if(stmt)

    elif isinstance(stmt, Assignment):
        return compile_assignment(stmt)


def compile_output(node):
    expr_code = compile_expr(node.expr)
    if str(expr_code).startswith('input('):
        return f"INPUT = {expr_code}\nprint(INPUT)"
    else:
        return f"print({expr_code})"


def compile_assignment(node):
    name = compile_expr(node.name)
    value = compile_expr(node.value)
    return f"{name} = {value}"


def compile_if(node):
    comp = compile_expr(node.condition)
    body = transpile_stmt(node.body)
    elsed = node.conelse
    #if isinstance(node.body, list):
     #   body = '\n'.join(str(body))

    if elsed:
        else_body = transpile_stmt(node.elsebody)
        return f"if {comp}:\n\t{body}\nelse:\n\t{else_body}"
    else:
        pass
    
    return f"if {comp}:\n\t{body}"


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
            return print(f"TypeError: {expr.t} is not a valid data type, only NUM, TXT, and BOOL are valid!")
    elif isinstance(expr, Random):
        return f"random.randint({expr._from.value}, {expr.to.value})"
    elif isinstance(expr, Input_Expr):
        return 'INPUT'
    elif isinstance(expr, Comparism):
        left_code = compile_expr(expr.left)
        right_code = compile_expr(expr.right)
        return f"{left_code} {expr.op} {right_code}"
    else:
        raise TypeError(f"Unknown expression type: {expr}")
