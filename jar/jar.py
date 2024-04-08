


class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity
        self.size=0

    def __str__(self):
        i="🍪"
        return self.size*i

    def deposit(self, n):
        self.add=self.size+n
        if self.add>self.capacity:
            raise ValueError
        return self.add

    def withdraw(self, n):
        self.sub=self.size-n
        if n>self.size:
            raise ValueError
        return self.sub

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        self._capacity=capacity
        if self._capacity<0:
            raise ValueError

    @property
    def size(self):
        self.size=self.size+self.add
        return self.size
    @size.setter
    def size(self,size):
        self._size=size
        if self._size>self.capacity:
            raise ValueError

def main():
    jar=Jar()
    jar.deposit(1)
    print(jar)
if __name__=="__main__":
    main()
