


class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity

    def __str__(self):
        return "🍪"

    def deposit(self, n):
        add=self.size+n
        if add>self.capacity:
            raise ValueError
        return add

    def withdraw(self, n):
        sub=self.size-n
        if n>self.size:
            raise ValueError
        return sub

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
        self.size=int()

def main():
    jar=Jar()
    jar.deposit(1)
    print(jar)
if __name__=="__main__":
    main()
