import pytest
from seasons import Birthdate

def test_validdate():
    assert Birthdate.convert((),(2024,4,6),(2024,4,7))==1440
