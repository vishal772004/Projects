import pytest
from fuel import convert,gauge

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0
def test_value_error():
    pytest.raises(ValueError)
def test_empty():
    assert gauge(0)=="E"
def test_full():
    assert gauge(100)=="F"
def test_half():
    assert gauge(66.5)==67
    assert gauge(65)==65
def test_fraction():
    assert convert("3/4")==75
    assert convert("1/2")==50
