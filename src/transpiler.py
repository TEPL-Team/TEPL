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

            elif isinstance(node, Function):
                compiled_code.append(compile_function(node))

            elif isinstance(node, While):
                compiled_code.append(compile_while(node))

            elif isinstance(node, Forever):
                compiled_code.append(compile_forever(node))

            elif isinstance(node, Exit):
                compiled_code.append(compile_exit(node))

            elif isinstance(node, Convert):
                compiled_code.append(compile_convert(node))

            elif isinstance(node, Call):
                compiled_code.append(compile_call(node))

            elif isinstance(node, Return):
                compiled_code.append(compile_return(node))

            elif isinstance(node, Delete):
                compiled_code.append(compile_delete(node))

            else:
                raise TypeError(
                    "Invalid AST root node. Expecting an 'Output' node or list of statements, but got "
                    + str(type(ast)))

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
        elif isinstance(ast, Function):
            compiled_code.append(compile_function(ast))
        elif isinstance(ast, While):
            compiled_code.append(compile_while(ast))
        elif isinstance(ast, Forever):
            compiled_code.append(compile_forever(ast))
        elif isinstance(ast, Exit):
            compiled_code.append(compile_exit(ast))
        elif isinstance(ast, Convert):
            compiled_code.append(compile_convert(ast))
        elif isinstance(ast, Call):
            compiled_code.append(compile_call(ast))
        elif isinstance(ast, Return):
            compiled_code.append(compile_return(ast))
        elif isinstance(ast, Delete):
            compiled_code.append(compile_delete(ast))
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

    elif isinstance(stmt, Function):
        return compile_function(stmt, ident_level)

    elif isinstance(stmt, While):
        return compile_while(stmt, ident_level)

    elif isinstance(stmt, Forever):
        return compile_forever(stmt, ident_level)

    elif isinstance(stmt, Exit):
        return compile_exit(stmt, ident_level)

    elif isinstance(stmt, Convert):
        return compile_convert(stmt, ident_level)

    elif isinstance(stmt, Call):
        return compile_call(stmt, ident_level)

    elif isinstance(stmt, Return):
        return compile_return(stmt, ident_level)

    elif isinstance(stmt, Delete):
        return compile_delete(stmt, ident_level)


def compile_output(stmt, indent_level=0):
    expr_code = compile_expr(stmt.expr)
    if str(expr_code).startswith('input('):
        return f"{'    ' * indent_level}INPUT = {expr_code}\n{'    ' * indent_level}print(INPUT)"
    else:
        return f"{'    ' * indent_level}print({expr_code})"


def compile_assignment(stmt, indent_level=0):
    name = compile_expr(stmt.name)
    value = compile_expr(stmt.value)
    if stmt.type is None:
        return f"{'    ' * indent_level}{name} = {value}"
    else:
        type = stmt.type
        if type.t_type.upper() == "LIST":
            return f"{'    ' * indent_level}{name} = [{value}]"
        else:
            return print(
                f"TypeError: Invalid assignment type, expected 'LIST', but got '{type.t_type.upper()}'!"
            )


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
    return f"{'    ' * indent_level}while True:\n{body}\n{'    ' * some2}if {comp}:\n{'    ' * some2}    break"


def compile_pause(stmt, indent_level=0):
    return f"{'    ' * indent_level}time.sleep({compile_expr(stmt.time)})"


def compile_function(stmt, ident_level=0):
    name = stmt.name
    body = transpile_stmt(stmt.body, ident_level + 1)
    if stmt.args is not None:
        args = ', '.join(stmt.args)
        return f"{'    ' * ident_level}def {name}({args}):\n{body}"
    else:
        return f"{'    ' * ident_level}def {name}():\n{body}"


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
    to_type = stmt.to_type
    if to_type.upper() == "NUM":
        return f"{'    ' * indent_level}{expr} = int({expr})"
    elif to_type.upper() == "DEC":
        return f"{'    ' * indent_level}{expr} = float({expr})"
    elif to_type.upper() == "TXT":
        return f"{'    ' * indent_level}{expr} = str({expr})"
    else:
        return print(
            f"Invalid type, {to_type}, expected 'NUM', 'DEC', or 'TXT'!")


def compile_call(stmt, indent_level=0):
    name = stmt.name
    args = stmt.args
    if args:
        args = compile_expr(list(args))
        return f"{'    ' * indent_level}{name}({args})"
    else:
        return f"{'    ' * indent_level}{name}()\n"


def compile_return(stmt, indent_level=0):
    expr = compile_expr(stmt.expr)
    return f"{'    ' * indent_level}return {expr}"


def compile_delete(stmt, indent_level=0):
    name = stmt.name
    return f"{'    ' * indent_level}del {name}"


def compile_expr(expr):
    if isinstance(expr, list):
        # If the expression is a list, compile each element in the list
        return ', '.join([str(compile_expr(e)) for e in expr])
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
        args = expr.args
        if args:
            args = compile_expr(list(args))
            return f"{name}({args})"
        else:
            return f"{name}()\n"
    elif isinstance(expr, Index):
        name = expr.name
        index = compile_expr(expr.index)
        return f"{name}[{index}]"
    else:
        raise TypeError(f"Unknown expression type: {expr}")
