
from twttr import shorten
def test_lowercase():
    assert shorten("Twitter")=="Twttr"

def test_uppercase():
    assert shorten("TWITTER")=="TWTTR"

def test_number():
    assert shorten("TWITTER2024")=="TWTTR2024"

def test_punctuation():
    assert shorten("TWITTER!!!")=="TWTTR!!!"
