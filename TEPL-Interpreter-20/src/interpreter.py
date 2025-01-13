from src.nodes import Set, Output, Binary, Number, Id, Random, Text, If, Condition, Input, While, Repeat
import random
from typing import Union

# Environment to store variable values
enviroment: dict[str, Union[int, float, str, None]] = {'INPUT': None}

# Interpret the list of statements
def interpret(body):
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
            for _ in range(times):
                interpret(body.body)

        else:
            raise Exception('Unknown statement type')

# Evaluate expressions
def expr(node):
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
        return enviroment[node.name]

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

    else:
        raise Exception('Unknown expression type')
