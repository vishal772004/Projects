class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError
        self._capacity=capacity
        self._size=0

    def __str__(self):
        i="🍪"
        return self.size*i

    def deposit(self, n):
        self.size=self.size+n
        if self.size>self.capacity:
            raise ValueError

    def withdraw(self, n):
        self.size=self.size-n
        if self.size<=0:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self,capacity=12):
        self._capacity=capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self):
        self._size=0

