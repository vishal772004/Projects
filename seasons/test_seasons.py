import pytest
from seasons import check

def test_validdate():
    assert check("2024-04-07")=="2024-04-07"

def test_invaliddate():
    with pytest.raises(ValueError):
        ("January 20,2001")


