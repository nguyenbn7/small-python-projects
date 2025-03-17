from collections import deque
from enum import Enum

_sep = "|"


def _is_operation(token: str):
    return token in "+-*/^"


def eval_math_expression(expression: str):
    postfix_expression = parse_to_postfix_expression(expression)
    return find_math_result(postfix_expression)


def parse_to_postfix_expression(expression: str):
    operation_stack = deque()
    new_expression = ""

    for idx, token in enumerate(expression):
        if token.isdigit():
            new_expression += token
            continue

        # Prevent double seperator
        if new_expression and new_expression[-1] != _sep:
            new_expression += _sep

        if token == " ":
            continue
        elif token == "(":
            operation_stack.append(token)
        elif token == ")":
            while operation_stack and operation_stack[-1] != "(":
                new_expression += f"{operation_stack.pop()}{_sep}"

            if operation_stack and operation_stack[-1] == "(":
                operation_stack.pop()
            else:
                raise Exception(
                    "Missing left parenthese for right parenthese at position: {idx}"
                )
        elif _is_operation(token):
            while operation_stack and (
                operation_stack[-1] != "("
                and (
                    _get_precedence(operation_stack[-1]) > _get_precedence(token)
                    or (
                        _get_precedence(operation_stack[-1]) == _get_precedence(token)
                        and _get_associativity(token) == _OperationAssociativity.LEFT
                    )
                )
            ):
                new_expression += f"{operation_stack.pop()}{_sep}"

            operation_stack.append(token)
        else:
            raise Exception(f"Invalid token {token} at position {idx}")

    while operation_stack:
        new_expression += f"{_sep}{operation_stack.pop()}"

    return new_expression


class _OperationAssociativity(Enum):
    LEFT = 1
    RIGHT = 2


def _get_associativity(operation: str):
    match operation:
        case "+" | "-" | "*" | "/":
            return _OperationAssociativity.LEFT
        case default:
            return _OperationAssociativity.RIGHT


def _get_precedence(char: str):
    match char:
        case "+" | "-":
            return 1
        case "*" | "/":
            return 2
        case "^":
            return 3
        case default:
            return -1


def find_math_result(postfix_expression: str):
    stack = deque()

    expression = postfix_expression.split(sep=_sep)

    for op in expression:
        if op.isdigit():
            stack.append(int(op))
        else:
            # standard formula like `lhs operator rhs = result`
            rhs = stack.pop()
            lhs = 0
            if stack:
                lhs = stack.pop()
            stack.append(_calculate(lhs, rhs, op))

    return stack.pop()


def _calculate(lhs: int | float, rhs: int | float, operation: str):
    match operation:
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


if __name__ == "__main__":
    print(
        find_math_result(parse_to_postfix_expression(" 3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"))
    )
