
class Rational:
    def __init__(self, n, d):
        self.n = n 
        self.d = d        
    def __add__(self, other):
        n = self.n*other.d + self.d*other.n
        d = self.d*other.d
        return Rational(n,d) 
    def __str__(self):
        return "Rational(%d,%d)" % (self.n,self.d)
    
    
