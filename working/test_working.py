import pytest
from working import convert

def test_validtime():
    assert convert("9:00 AM to 9:00 PM")==("09:00 to 21:00")
    assert convert("12:00 AM to 12:00 PM")==("00:00 to 12:00")
    assert convert("10:30 AM to 5:20 PM")==("10:30 to 17:20")
    assert convert("9 AM to 9 PM")==("09:00 to 21:00")
def test_inavlidtime():
    with pytest.raises(ValueError):
        convert("13:00 AM to 13:00 PM")
        convert("9:00 AM - 9:00 PM")
        convert("12 AM -12 PM")
        convert("12 AM 12 PM")

