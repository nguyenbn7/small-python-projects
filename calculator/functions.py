from collections import deque
from enum import Enum


class OperatorAssociativity(Enum):
    LEFT = 1
    RIGHT = 2


def is_operator(token: str):
    """
    Returns true if given character is an operator +, -, *, /, ^
    """
    return token in "+-*/^"


def get_operator_associativity(operation: str):
    match operation:
        case "+" | "-" | "*" | "/":
            return OperatorAssociativity.LEFT
        case default:
            return OperatorAssociativity.RIGHT


def get_operator_precedence(token: str):
    match token:
        case "+" | "-":
            return 1
        case "*" | "/":
            return 2
        case "^":
            return 3
        case default:
            return -1


def perform_math_calculation(postfix_expression: str, seperator="|"):
    stack = deque()

    expression = postfix_expression.split(sep=seperator)

    for op in expression:
        if op.isdigit():
            stack.append(int(op))
        else:
            # standard formula like `lhs operator rhs = result`
            rhs = stack.pop()
            lhs = 0
            if stack:
                lhs = stack.pop()
            stack.append(perform_binary_operation(lhs, rhs, op))

    return stack.pop()


def perform_binary_operation(lhs: int | float, rhs: int | float, operator: str):
    match operator:
        case "+":
            return lhs + rhs
        case "-":
            return lhs - rhs
        case "*":
            return lhs * rhs
        case "/":
            return lhs / rhs
        case "^":
            return lhs**rhs
        case default:
            raise Exception("Invalid operator")


def convert_to_postfix_expression(math_expression: str, seperator="|"):
    operation_stack = deque()
    new_expression = ""

    for idx, token in enumerate(math_expression):
        if token.isdigit():
            new_expression += token
            continue

        # Prevent double seperator
        if new_expression and new_expression[-1] != seperator:
            new_expression += seperator

        if token == " ":
            continue
        elif token == "(":
            operation_stack.append(token)
        elif token == ")":
            while operation_stack and operation_stack[-1] != "(":
                new_expression += f"{operation_stack.pop()}{seperator}"

            if operation_stack and operation_stack[-1] == "(":
                operation_stack.pop()
            else:
                raise Exception(
                    "Missing left parenthese for right parenthese at position: {idx}"
                )
        elif is_operator(token):
            while operation_stack and (
                operation_stack[-1] != "("
                and (
                    get_operator_precedence(operation_stack[-1])
                    > get_operator_precedence(token)
                    or (
                        get_operator_precedence(operation_stack[-1])
                        == get_operator_precedence(token)
                        and get_operator_associativity(token)
                        == OperatorAssociativity.LEFT
                    )
                )
            ):
                new_expression += f"{operation_stack.pop()}{seperator}"

            operation_stack.append(token)
        else:
            raise Exception(f"Invalid token {token} at position {idx}")

    while operation_stack:
        new_expression += f"{seperator}{operation_stack.pop()}"

    return new_expression


def calculate(math_expression: str):
    postfix_expression = convert_to_postfix_expression(math_expression)
    return perform_math_calculation(postfix_expression)
