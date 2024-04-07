import pytest
from seasons import convert

def test_validdate():
    assert convert((2024-4-7),(2024-4-8))==1440
    assert convert((2024-4-6),(2024-4-8))==2880
    #assert convert((2023-4-8),(2024-4-8))==525600

