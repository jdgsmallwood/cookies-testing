from example_functions import add_three, minus_three

import pytest

arguments = "smaller, larger"
parameters = [(-4, -1), (-1, 2), (0, 3), (9, 12)]  # Differ by 3.

@pytest.mark.parametrize(arguments, parameters)
def test_add_three(smaller, larger):
    assert add_three(smaller) == larger, "smaller + 3 should equal larger"


@pytest.mark.parametrize(arguments, parameters)
def test_minus_three(larger, smaller):
    assert minus_three(larger) == smaller, "larger - 3 should equal smaller"


@pytest.mark.parametrize("test_input", [-6, -4, -1, 0, 3, 9])
def test_reversible_inverse(test_input):
    """The function minus_three is the left and right inverse of add_three."""
    left_inverse = minus_three(add_three(test_input))
    right_inverse = add_three(minus_three(test_input))
    assert left_inverse == test_input == right_inverse



