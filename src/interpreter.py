from src.nodes import Set, Output, Binary, Number, Id, Random, Text, If, Condition, Input, While, Repeat, Convert, And, Or
import random
from typing import Union

# Environment to store variable values
enviroment: dict[str, Union[int, float, str, None]] = {'INPUT': None}

# Interpret the list of statements
def interpret(body):
    try:
        if isinstance(body, list):
            for stmt in body:
                interpret(stmt)
        else:
            if isinstance(body, Set):
                name = body.name.name
                value = expr(body.value)
                enviroment[name] = value

            elif isinstance(body, Output):
                value = expr(body.value)
                print(value)

            elif isinstance(body, If):
                condition = expr(body.condition)
                if condition:
                    interpret(body.body)

            elif isinstance(body, Input):
                # Ask the input question, process, and store the result
                question = expr(body.question)  # Input prompt/question

                # Get input from user
                user_input = input(str(question))

                # Try to cast the input to a number if possible, otherwise keep it as a string
                try:
                    if '.' in user_input:
                        enviroment['INPUT'] = float(user_input)
                    else:
                        enviroment['INPUT'] = int(user_input)
                except ValueError:
                    enviroment['INPUT'] = user_input

            elif isinstance(body, While):
                cond = expr(body.cond)
                while cond:
                    interpret(body.body)
                    cond = expr(body.cond)

            elif isinstance(body, Repeat):
                times = expr(body.times)
                if not isinstance(times, int):
                    raise TypeError(f"Expected 'times' to be an integer, got {type(times).__name__}")
                for i in range(1, times + 1):
                    enviroment[body.id.name] = i
                    interpret(body.body)

            else:
                raise Exception('Unknown statement type')
    except Exception as e:
        print(f"Interpreter error: {e}")

# Evaluate expressions
def expr(node):
    try:
        if isinstance(node, Number):
            return node.value

        elif isinstance(node, Binary):
            left = expr(node.left)
            right = expr(node.right)

            if node.op == '+':
                return left + right

            elif node.op == '-':
                return left - right

            elif node.op == '*':
                return left * right

            elif node.op == '/':
                return left / right

        elif isinstance(node, Id):
            return enviroment.get(node.name, None)

        elif isinstance(node, Random):
            if node.type.lower() == 'number':
                return random.randint(expr(node.f), expr(node.to))

        elif isinstance(node, Text):
            return node.value

        elif isinstance(node, Condition):
            left = expr(node.left)
            right = expr(node.right)

            if node.op == '==':
                return left == right

            elif node.op == '!=':
                return left != right

            elif node.op == '<':
                return left < right

            elif node.op == '>':
                return left > right

            elif node.op == '<=':
                return left <= right

            elif node.op == '>=':
                return left >= right

        elif isinstance(node, Convert):
            value = expr(node.value)
            datatype = node.datatype.upper()
            if datatype == 'NUM':
                return int(value)
            elif datatype == 'TXT':
                return str(value)
            else:
                raise TypeError(f"Expected 'NUM' or 'TXT' as datatype, got {datatype}")

        elif isinstance(node, And):
            return expr(node.left) and expr(node.right)

        elif isinstance(node, Or):
            return expr(node.left) or expr(node.right)

        else:
            raise Exception('Unknown expression type')
    except Exception as e:
        print(f"Expression error: {e}")
        return None
