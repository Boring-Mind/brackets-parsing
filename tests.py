import pytest

from main import BracketValidator


@pytest.mark.parametrize(
    "input_string,expected_result",
    [
        ("([<>])", True),
        ("()[]<{}>", True),
        ("[<>()[(<>)]]", True),
        ("([)]", False),
        ("[[]", False),
        ("<(}>", False),
        (">", False),
        ("", True),
    ],
)
def test_bracket_validator__is_valid__default_case(
    input_string: str, expected_result: bool
):
    actual_result = BracketValidator(input_string).is_valid()

    assert expected_result == actual_result
