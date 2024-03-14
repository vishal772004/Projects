
from twttr import shorten
def test_lowercase():
    assert shorten("Twitter")=="Twttr"

def test_uppercase():
    assert shorten("TWITTER")=="TWTTR"
