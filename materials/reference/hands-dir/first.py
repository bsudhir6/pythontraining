import sys
import pkg.mex

s = sys.argv[1]
ca = list(s)
print(pkg.mex.freq(ca))
   
wa = s.split()   
print(pkg.mex.freq(wa))  

