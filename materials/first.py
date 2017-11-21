import sys 

#a = sys.argv[1]
#b = sys.argv[2]

#print(int(a) + int(b))

########################
s = "Hello World"
#H - 1
#e - 1
#l - 3

#take each char(ch) from s
for ch in s:
    #initialize counter 
    cnt = 0
    #take again each char(ch1) from s 
    for ch1 in s:
        #if ch and ch1 are same,
        if ch == ch1:
            #increment counter 
            cnt = cnt + 1
    #print ch and counter 
    print(ch,"-",cnt)
    
#########################################
#[]  list - Mutable, Indexing-A, Duplicates - A, IO - A 
#()      tuple - Immutable, ------above------
#
#{}  set - Mutable , Indexing - NA, Duplicates-NA, IO-NA 
#        frozenset - Immutable , ---- above----
#-------------------------
#dict 
#
#--------------------
#create empty list 
#take each element(e) from l 
#    Check if e is odd
#    then only append to empty list 
#    
    
s = '[1,2,3,4,5]'
res = []
#strip s with '[]' and then split with ','
#tmp1 = s.strip('[]')

for e in s.strip('[]').split(','):
    res.append(int(e)) 
    
    
    
    
    













    
    
    
    
    
    
    
    
