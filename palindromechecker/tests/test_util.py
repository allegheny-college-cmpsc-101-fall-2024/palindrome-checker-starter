# TODO: Add the required docstring and any required imports of objects

# TODO: Add the necessary import statements to access the modules under test

# TODO: Add comments to the test cases to explain how the tests works


def test_human_readable_boolean_true():
    """Ensure that a human-readable true boolean works correctly."""
    true_value = True
    true_value_human_readable = util.get_human_readable_boolean(true_value)
    assert true_value_human_readable == "Yes, it is!"


def test_human_readable_boolean_false():
    """Ensure that a human-readable false boolean works correctly."""
    # TODO: add a test case that follows the provided example
