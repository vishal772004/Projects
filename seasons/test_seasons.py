import pytest
from seasons import convert

def test_validdate():
    assert convert((2024-4-2),(2024-4-7))==1440
