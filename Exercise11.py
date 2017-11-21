##create empty dictionary d
##Take each element ch from s
##    if ch is present in d,
##        then increment it's value
##    if not
##        then initialize the key ch with 1
s="Hello World"
d = {}
for ch in s:
    cnt = 0    
    if ch in d:
        d[ch] = d[ch] + 1
    else:
        d[ch] = 1
print(d)
##Output
##{'o': 2, 'd': 1, 'r': 1, 'l': 3, 'e': 1, 'W': 1, 'H': 1, ' ': 1}
