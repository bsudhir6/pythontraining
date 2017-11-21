import functools 

@functools.total_ordering
class MyInt:
    def __init__(self, v):
        self.value = v 
    def __add__(self, other):
        return MyInt(self.value + other.value) 
    def __sub__(self, other):
        return MyInt(self.value - other.value) 
    def __str__(self):
        return "MyInt(%d)" % (self.value,)
    def __eq__(self, other):
        return self.value == other.value      
    def __lt__(self, other):
        return self.value < other.value      
    def __call__(self, power):
        return MyInt(self.value ** power)