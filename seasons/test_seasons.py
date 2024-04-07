import pytest
from seasons import check

def test_validdate():
    assert check("2024","04","07")==("2024-04-07")


