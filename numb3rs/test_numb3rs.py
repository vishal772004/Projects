import pytest
from numb3rs import validate

def test_valid_ip():
    assert validate("1.2.3.4") ==True
    assert validate("255.255.255.255")==True
    assert validate("10.200.199.37")==True
def test_invalid_ip():
    assert validate("300.274.574.256")==False
def test_invalid():
    with pytest.raises(ValueError):
        validate("cat")

