##create empty list
##take each element (e) from l
##    Check if e is odd
##    then only append to empty list
l = [1,2,3,4]
res = []
for e in l:
    if e % 2 != 0:
        res.append(e*e) # map filtering
print(res)
    
