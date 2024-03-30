import pytest
from working import convert

def test_validtime():
    assert convert("9:00 AM to 9:00 PM")==("9:00 to 21:00")
    assert convert("12:00 AM to 12:00 PM")==("12:00 to 12:00")
    assert convert("10:30 AM to 5:20 PM")==("10:30 to 17:20")

