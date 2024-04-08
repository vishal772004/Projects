from jar import Jar


def test_init():
    jar=Jar()
    assert jar.init(12)==None


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
    assert jar.deposit(1) == 1
    assert jar.deposit(5) == 6


def test_withdraw():
    jar=Jar()
    assert jar.withdraw(1) == 1
    assert jar.withdraw(5) == 5
