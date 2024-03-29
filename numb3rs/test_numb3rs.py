import pytest
from numb3rs import validate

def valid_ip():
    assert validate("1.2.3.4") ==True
    assert validate()
