
from um import count

def count_once():
    assert count("um")==1
    assert count("um?")==1
    assert count("Um, thanks for the album")==1

def count_twice():
    assert count("Um, thanks, um...")==2
