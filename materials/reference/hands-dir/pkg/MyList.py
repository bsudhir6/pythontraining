import math 


class MyList(list):
    def __init__(self, v):
        list.__init__(self,v) #super().__init__(v)
    def mean(self):
        return sum(self)/len(self)
    def mode(self):
        d = { self.count(e):e for e in self}
        return d[max(d)]
    def mode1(self):
        return max(self, key=self.count)
    def median(self):
        l = sorted(self)
        n = len(self)
        if n % 2 == 1:
            return l[n//2]
        else:
            return (l[n//2-1] + l[n//2])/2
    def sd(self):
        m = self.mean()
        return math.sqrt(sum((e-m)**2 for e in self)/len(self))
        
        
        
        