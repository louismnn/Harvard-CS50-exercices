class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._n = 0

    def __str__(self):
        return "🍪" * self._n 
        
    def deposit(self, n):
        if n < 0:
            raise ValueError
        if self._n + n > self._capacity:
            raise ValueError
        self._n += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError
        if self._n - n < 0:
            raise ValueError
        self._n -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError
        self._capacity = value

    @property
    def size(self):
        return self._n

def main():
    j = Jar()

    print(j)

if __name__=='__main__':
    main()