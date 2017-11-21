def longest(lst):
    max=''
    for e in lst:
        if len(e) > len(max):
            max=e
    return max

print(longest(['sud','sudh', 'sudhir']))
            
