import functools

@functools.total_ordering
class MyInt:
    def __init__(self, v):
        self.v = v 
    def __add__(self, other):
        return MyInt(self.v + other.v) 
    def __str__(self):
        return "MyInt(%d)" % (self.v, )
    def __eq__(self, other):
        return self.v == other.v
    def __lt__(self, other):
        return self.v < other.v
        
        
        
class Rational:
    def __init__(self, n, d):
        self.n = n 
        self.d = d
    def __add__(self, other):
        n = self.n * other.d + other.n * self.d
        d = self.d * other.d
        return Rational(n,d) 
    def __str__(self):
        return "Rational(%d, %d)" % (self.n, self.d)
    def __eq__(self, other):
        f1 = self.n/self.d
        f2 = other.n/other.d
        return f1 == f2
    