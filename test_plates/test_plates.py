from plates import is_valid

def test_starts_with_alphabet():
    assert is_valid("12ABCD")==False
    assert is_valid("ABCDEF")==True

def test_length():
    assert is_valid("ABC1234")==False
    assert is_valid("A")==False

def test_not_alphanumeric():
    assert is_valid("ABC!@#")==False
    assert is_valid("ABC$%^")==False
    assert is_valid("ABC&*?")==False


def test_not_starting_from_zero():
    assert is_valid("ABC012")==False

def test_ending_with_digit():
    assert is_valid("ABC12A")==False


