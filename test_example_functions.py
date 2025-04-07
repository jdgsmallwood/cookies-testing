from example_functions import add_three, minus_three

def test_additive_inverse():
    """The function minus_three is the additive inverse of add_three."""
    for x in [-5, 1, 0, 1, 9]:
        assert x == add_three(minus_three(x)), "Should return original number."

