l = [1,2,3,4]
res = []
for e in l:
    ##res.append(e * e)
    ##res += [e*e]
    res = res + [e*e]
print(res)

##Pseudo Code
##create empty list
##take each element(e) from l
##    square it
##    and append to empty list
