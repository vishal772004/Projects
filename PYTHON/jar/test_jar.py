from jar import Jar


def test_init():
    jar=Jar()
    jar.capacity =12
    jar=Jar(5)
    jar.capacity =5

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar()
    jar.deposit(5)
    assert jar.size==5
    jar.deposit(5)
    assert jar.size==10

def test_withdraw():
    jar2=Jar()
    jar2.deposit(10)
    jar2.withdraw(5)
    assert jar2.size==5
    jar2.withdraw(1)
    assert jar2.size == 4

