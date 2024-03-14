from bank import value

def test_fullgreeting():
    assert value("Hello")==0
def test_halfgreeting():
    assert value("Hey")==20
def test_greeting_not_including_h():
    assert value("What's up")==100
