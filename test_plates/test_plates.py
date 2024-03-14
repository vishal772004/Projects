from plates import isvalid

def test_length():
    assert isvalid("ABC123")==True

def test_not_alphanumeric():
    assert isvalid("!@#$%&*")==False

def test_not_starting_from_zero():
    assert isvalid("ABC012")==False

def 
