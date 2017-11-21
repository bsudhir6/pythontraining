s = '[1,2,3,4,5]'
res=[]
s = s.strip("[]")
s = s.split(",")
for e in s:    
    res.append(int(e))
print(res)

##s='[1,2,3,4,5]'
##create empty list
##strip '[', ']' charecters out of s
##split s with ','
##Take each element from above
##    convert element to int
##    and append to empty list
