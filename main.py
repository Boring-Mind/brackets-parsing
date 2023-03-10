from collections import deque


class BracketValidator:
    def __init__(self, input_string: str):
        self._input_string = input_string
        self._stack = deque()

    def _check_closing_bracket(self, opening_bracket: str) -> bool:
        """Check if closing bracket has paired opening bracket.

        Function returns True if closing bracket has opening one.
        It returns False if it hasn't.
        """
        try:
            prev_char = self._stack.pop()
        except IndexError:
            # There are no chars in the stack, so there are no open bracket left
            return False
        if prev_char != opening_bracket:
            return False
        return True

    def is_valid(self) -> bool:
        if self._input_string == "":
            return True

        for char in self._input_string:
            if char in "[({<":
                self._stack.append(char)
            elif char == "]":
                if not self._check_closing_bracket("["):
                    return False
            elif char == ")":
                if not self._check_closing_bracket("("):
                    return False
            elif char == ">":
                if not self._check_closing_bracket("<"):
                    return False
            elif char == "}":
                if not self._check_closing_bracket("{"):
                    return False

        if len(self._stack) > 0:
            # If there are some characters left in the stack after processing,
            # it means that some bracket was not closed.
            return False
        # If the processing was ended and there is no items in stack left,
        # then all open brackets were closed.
        return True
