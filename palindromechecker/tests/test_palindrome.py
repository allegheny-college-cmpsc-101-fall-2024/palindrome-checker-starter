# TODO: Add the required docstring and any required imports of objects

# TODO: Add the necessary import statements to access the modules under test

# TODO: Add comments to the test cases to explain how the tests works


def test_short_palindrome_word_recursive():
    """Ensure that a short word of "civic" works correctly with recursive."""
    word = "civic"
    result = palindrome.is_palindrome_recursive(word)
    assert result is True


def test_short_not_palindrome_word_recursive():
    """Ensure that a short word of "taylor" does not work correctly with recursive."""
    # TODO: implement this test case using the provided example


def test_short_palindrome_word_reverse():
    """Ensure that a short word of "civic" works correctly with reverse."""
    # TODO: implement this test case using the provided example


def test_short_not_palindrome_word_reverse():
    """Ensure that a short word of "taylor" does not work correctly with reverse."""
    # TODO: implement this test case using the provided example
