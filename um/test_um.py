
from um import count

def count_once():
    assert convert("um")==1
    assert convert("um?")==1
    assert convert("Um, thanks for the album")==1

def count_twice():
    assert convert("Um, thanks, um...")==2
