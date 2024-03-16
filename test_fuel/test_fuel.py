import pytest
from fuel import convert,gauge

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("5/3")
def test_valid():
    assert convert("0/1")==0 and gauge(0)=="E"
    assert convert("99/100")==99 and gauge(99)=="F"
    assert convert("1/100")==1 and gauge(1)=="E"
    assert convert("3/4")==75 and gauge(75)=="75%"
    assert convert("1/2")==50 and gauge(50)=="50%"






