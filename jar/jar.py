class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity
        self.size=0

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
        return self.capacity
    @capacity.setter
    def capacity(self,capacity=12):
        self._capacity=capacity

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self,size):
        self._size=size

def main():
    jar=Jar()
    jar.deposit(1)
    print(jar)
if __name__=="__main__":
    main()
