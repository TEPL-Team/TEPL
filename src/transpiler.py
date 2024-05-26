from parser import parser
from parser import __error__
from nodes import *


def transpile(ast):
    compiled_code = ['import random', 'import time', 'INPUT = None']

    if isinstance(ast, list):
        for node in ast:
            compiled_code.append(transpile_stmt(node))
    else:
        compiled_code.append(transpile_stmt(ast))

    return '\n'.join(compiled_code)


def transpile_stmt(stmt, indent_level=0):
    if isinstance(stmt, list):
        return '\n'.join([transpile_stmt(s, indent_level) for s in stmt])

    indent = '    ' * indent_level
    if isinstance(stmt, Output):
        return compile_output(stmt, indent_level)
    elif isinstance(stmt, If):
        return compile_if(stmt, indent_level)
    elif isinstance(stmt, Assignment):
        return compile_assignment(stmt, indent_level)
    elif isinstance(stmt, Repeat):
        return compile_repeat(stmt, indent_level)
    elif isinstance(stmt, Pause):
        return compile_pause(stmt, indent_level)
    elif isinstance(stmt, Function):
        return compile_function(stmt, indent_level)
    elif isinstance(stmt, While):
        return compile_while(stmt, indent_level)
    elif isinstance(stmt, Forever):
        return compile_forever(stmt, indent_level)
    elif isinstance(stmt, Exit):
        return compile_exit(stmt, indent_level)
    elif isinstance(stmt, Convert):
        return compile_convert(stmt, indent_level)
    elif isinstance(stmt, Call):
        return compile_call(stmt, indent_level)
    elif isinstance(stmt, Return):
        return compile_return(stmt, indent_level)
    elif isinstance(stmt, Delete):
        return compile_delete(stmt, indent_level)
    elif isinstance(stmt, Clear):
        return compile_clear(stmt, indent_level)
    elif isinstance(stmt, For):
        return compile_for(stmt, indent_level)
    else:
        raise TypeError(f"Unknown statement type: {type(stmt)}")


def compile_output(stmt, indent_level=0):
    expr_code = compile_expr(stmt.expr)
    indent = '    ' * indent_level
    if str(expr_code).startswith('input('):
        return f"{indent}INPUT = {expr_code}\n{indent}print(INPUT)"
    else:
        return f"{indent}print({expr_code})"


def compile_assignment(stmt, indent_level=0):
    name = compile_expr(stmt.name)
    value = compile_expr(stmt.value)
    indent = '    ' * indent_level
    if stmt.type is None:
        return f"{indent}{name} = {value}"
    else:
        type = stmt.type
        if type.t_type.upper() == "LIST":
            return f"{indent}{name} = [{value}]"
        else:
            raise TypeError(
                f"Invalid assignment type, expected 'LIST', but got '{type.t_type.upper()}'!"
            )


def compile_if(stmt, indent_level=0):
    comp = compile_expr(stmt.condition)
    body = transpile_stmt(stmt.body, indent_level + 1)
    indent = '    ' * indent_level
    if stmt.conelse:
        else_body = transpile_stmt(stmt.elsebody, indent_level + 1)
        return f"{indent}if {comp}:\n{body}\n{indent}else:\n{else_body}"
    else:
        return f"{indent}if {comp}:\n{body}"


def compile_repeat(stmt, indent_level=0):
    comp = compile_expr(stmt.condition)
    body = transpile_stmt(stmt.body, indent_level + 1)
    indent = '    ' * indent_level
    inner_indent = '    ' * (indent_level + 1)
    return f"{indent}while True:\n{body}\n{inner_indent}if {comp}:\n{inner_indent}    break"


def compile_pause(stmt, indent_level=0):
    return f"{'    ' * indent_level}time.sleep({compile_expr(stmt.time)})"


def compile_function(stmt, indent_level=0):
    name = stmt.name
    body = transpile_stmt(stmt.body, indent_level + 1)
    indent = '    ' * indent_level
    if stmt.args:
        args = ', '.join(stmt.args)
        return f"{indent}def {name}({args}):\n{body}"
    else:
        return f"{indent}def {name}():\n{body}"


def compile_while(stmt, indent_level=0):
    comp = compile_expr(stmt.condition)
    body = transpile_stmt(stmt.body, indent_level + 1)
    return f"{'    ' * indent_level}while {comp}:\n{body}"


def compile_forever(stmt, indent_level=0):
    body = transpile_stmt(stmt.body, indent_level + 1)
    return f"{'    ' * indent_level}while True:\n{body}"


def compile_exit(stmt, indent_level=0):
    return f"{'    ' * indent_level}break"


def compile_convert(stmt, indent_level=0):
    expr = compile_expr(stmt.expr)
    to_type = stmt.to_type.upper()
    indent = '    ' * indent_level
    if to_type == "NUM":
        return f"{indent}{expr} = int({expr})"
    elif to_type == "DEC":
        return f"{indent}{expr} = float({expr})"
    elif to_type == "TXT":
        return f"{indent}{expr} = str({expr})"
    else:
        raise TypeError(
            f"Invalid type, {to_type}, expected 'NUM', 'DEC', or 'TXT'!")


def compile_call(stmt, indent_level=0):
    name = stmt.name
    indent = '    ' * indent_level
    if stmt.args:
        args = compile_expr(stmt.args)
        return f"{indent}{name}({args})"
    else:
        return f"{indent}{name}()"


def compile_return(stmt, indent_level=0):
    expr = compile_expr(stmt.expr)
    return f"{'    ' * indent_level}return {expr}"


def compile_delete(stmt, indent_level=0):
    name = compile_expr(stmt.name)
    indent = '    ' * indent_level
    if stmt.index is None:
        return f"{indent}del {name}"
    else:
        index = compile_expr(stmt.index)
        return f"{indent}{name}.pop({index} - 1)"


def compile_clear(stmt, indent_level=0):
    name = compile_expr(stmt._list)
    return f"{'    ' * indent_level}{name}.clear()"


def compile_for(stmt, indent_level=0):
    name = stmt.name
    times = compile_expr(stmt.times)
    body = transpile_stmt(stmt.body, indent_level + 1)
    indent = '    ' * indent_level
    return f"{indent}for {name} in range(1, {times+1}):\n{body}"


def compile_expr(expr):
    if isinstance(expr, list):
        return ', '.join([str(compile_expr(e)) for e in expr])
    elif isinstance(expr, Number):
        return expr.value
    elif isinstance(expr, BinOp):
        left_code = compile_expr(expr.left)
        right_code = compile_expr(expr.right)
        return f"{left_code} {expr.op} {right_code}"
    elif isinstance(expr, Identifier):
        return expr.name
    elif isinstance(expr, Boolean):
        return 'True' if expr.value.lower() == 'yes' else 'False'
    elif isinstance(expr, Text):
        return f"{str(expr.text)}"
    elif isinstance(expr, Input):
        q = expr.q
        t = expr.t.upper()
        if t == 'NUM':
            return f"int(input({q}))"
        elif t == 'DEC':
            return f"float(input({q}))"
        elif t == 'TXT':
            return f"input({q})"
        elif t == 'BOOL':
            return f"bool(input({q}))"
        else:
            raise TypeError(
                f"TypeError: {t} is not a valid data type, only 'NUM', 'TXT', 'DEC', and 'BOOL' are valid!"
            )
    elif isinstance(expr, Random):
        return f"random.randint({expr._from.value}, {expr.to.value})"
    elif isinstance(expr, Input_Expr):
        return 'INPUT'
    elif isinstance(expr, Comparism):
        left_code = compile_expr(expr.left)
        right_code = compile_expr(expr.right)
        op = expr.op
        if op in ['AND', 'OR']:
            return f"({left_code} {op.lower()} {right_code})"
        elif op == 'NOT':
            return f"not {right_code}"
        elif op == 'IN':
            return f"({left_code} in {right_code})"
        else:
            return f"{left_code} {op} {right_code}"
    elif isinstance(expr, Substring):
        from_expr = compile_expr(expr.from_expr)
        to_expr = compile_expr(expr.to_expr)
        string = compile_expr(expr.string)
        return f"{string}[{from_expr - 1}:{to_expr}]"
    elif isinstance(expr, Length):
        expr_code = compile_expr(expr.expr)
        return f"len({expr_code})"
    elif isinstance(expr, Find):
        char = compile_expr(expr.char)
        string = compile_expr(expr.string)
        return f"{string}.count({char})"
    elif isinstance(expr, Call):
        name = expr.name
        if expr.args:
            args = compile_expr(list(expr.args))
            return f"{name}({args})"
        else:
            return f"{name}()"
    elif isinstance(expr, Index):
        name = compile_expr(expr.name)
        index = compile_expr(expr.index)
        return f"{name}[{index} - 1]"
    else:
        raise TypeError(f"Unknown expression type: {type(expr)}")
