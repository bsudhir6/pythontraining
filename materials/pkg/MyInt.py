import functools
@functools.total_ordering
class MyInt:    
        def __init__(self, v):
            self.value = v
        def __add__(self, other):
            return MyInt(self.value + other.value)
        def __sub__(self, other):
            return MyInt(self.value - other.value)
        def __eq__(self,other):
            return self.value == other.value
        def __lt__(self,other):
            return self.value < other.value
        def __le__(self,other):
            return self.value <= other.value
        def __str__(self):
            return "MyInt(%d)" %(self.value,)
class Fraction:
        def __init__(self, a, b):
                self.value1 = a
                self.value2 = b
        def __add__(self, other):
                numerator = (self.value1 * other.value2)+(self.value2 * other.value1)
                denominator = (self.value2 * other.value2)
                return Fraction(numerator, denominator)
        def __str__(self):
                return "Fraction(%d , %d)" % (self.value1, self.value2)
        
        
        
            
