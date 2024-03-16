import pytest
from fuel import convert,gauge

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("5/3")



