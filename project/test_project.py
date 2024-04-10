
from project import option1

def test_option1():
    assert option1(1,"Action,Adventure") == True
    assert option1(2,"Action,Adventure,Drama") == True
    assert option1(3,"Drama,Crime") == True
    assert option1(4,"Action,Crime") == True
    assert option1(5,"History,Crime") == True
    assert option1(6,"Comedy") == True
    assert option1(7,"Fantasy") == True
    assert option1(8,"Animation") == True


def test_invalid_option1():
    assert option1(1,"Adventure,Drama") == None
    assert option1(2,"Action,Drama") == None
    assert option1(3,"Crime") == None
    assert option1(4,"Action") == None
    assert option1(5,"Crime") == None
    assert option1(6,"Action") == None
    assert option1(7,"Adventure") == None
    assert option1(8,"Fantasy") == None
