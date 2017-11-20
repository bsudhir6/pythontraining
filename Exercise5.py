s = "Hello World"
for e in s:
    counter=0
    for f in s:
        if e == f :
            counter = counter + 1
    print (e,"-",counter)


####Psuedo Code
##    take each char(ch) from s
##        initialize counter
##        take again each char(ch1) from s
##            if ch and ch1 are same
##                increment counter
##        print ch and counter
