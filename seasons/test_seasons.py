import pytest
from seasons import convert

def test_validdate():
    assert convert((2024,04,06),(2024,04,07))==1440
