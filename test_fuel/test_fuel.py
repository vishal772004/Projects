import pytest
from fuel import convert,gauge

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0
def test_value_error():
    raise ValueError


