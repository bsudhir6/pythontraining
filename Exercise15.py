##function to find longest word in a list of strings
def longest(lst):
    res={len(e):e for e in lst}
    longestKey = max(res.keys())
    return res[longestKey]

print(longest(['sud','sudhifrr','sudhipdfrr']))
