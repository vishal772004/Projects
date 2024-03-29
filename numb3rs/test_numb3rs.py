import pytest
from numb3rs import validate

def test_valid_ip():
    assert validate("1.2.3.4") ==True
    assert validate("255.255.255.255")==True
    assert validate("10.200.199.37")==True
def test_invalid_ip():
    assert validate("300.274.574.256")==False
def test_first():
    assert validate("200.500.300.400")==False
def test_second():
    assert validate("600.100.365.456")==False
def test_third():
    assert validate("391.429.120.600")==False
def test_fourth():
    assert validate("981.256.399.10")

