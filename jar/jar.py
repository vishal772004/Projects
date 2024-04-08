class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        if self.capacity<0:
            raise ValueError
        return self._capacity

    @property
    def size(self):
        ...

def main():
    ...
if __name__=="__main__":
    main()
