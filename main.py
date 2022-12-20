from collections import deque


class BracketValidator:
    def __init__(self, input_string: str):
        self._input_string = input_string

    def is_valid(self) -> bool:
        stack = deque()

        if self._input_string == "":
            return True

        for char in self._input_string:
            if char in "[({<":
                stack.append(char)
            elif char == "]":
                try:
                    prev_char = stack.pop()
                except IndexError:
                    # There are no chars in the stack, so there are no open bracket left
                    return False
                if prev_char != "[":
                    return False
            elif char == ")":
                try:
                    prev_char = stack.pop()
                except IndexError:
                    # There are no chars in the stack, so there are no open bracket left
                    return False
                if prev_char != "(":
                    return False
            elif char == ">":
                try:
                    prev_char = stack.pop()
                except IndexError:
                    # There are no chars in the stack, so there are no open bracket left
                    return False
                if prev_char != "<":
                    return False
            elif char == "}":
                try:
                    prev_char = stack.pop()
                except IndexError:
                    # There are no chars in the stack, so there are no open bracket left
                    return False
                if prev_char != "{":
                    return False

        if len(stack) > 0:
            # If there are some characters left in the stack after processing,
            # it means that some bracket was not closed.
            return False
        # If the processing was ended and there is no items in stack left,
        # then all open brackets were closed.
        return True
