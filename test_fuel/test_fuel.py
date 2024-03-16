import pytest
from fuel import convert,gauge

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_value_error():
    with pytest.raises(ValueError):
        convert("cat")
def test_empty():
    assert gauge(0)=="E"
    assert gauge(1)=="E"
def test_full():
    assert gauge(100)=="F"
    assert gauge(99)=="F"
def test_half():
    assert gauge(66.5)=="67%"
    assert gauge(65)=="65%"
def test_fraction():
    assert convert("3/4")==75
    assert convert("1/2")==50
    assert convert("0/1")==0
    assert convert("1/100")==1
    assert convert("99/100")==99


