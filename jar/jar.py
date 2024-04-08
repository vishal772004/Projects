class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise VallueError
        self._capacity=capacity
        self._size=0

    def __str__(self):
        i="🍪"
        return self.size*i

    def deposit(self, n):
        self.size=self.size+n
        if self.size>self.capacity:
            raise ValueError
        return self.size

    def withdraw(self, n):
        self.size=self.size-n
        if self.size<=0:
            raise ValueError
        return self.size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

