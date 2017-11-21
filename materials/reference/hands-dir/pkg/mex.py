
def square(x):
    '''First function
    does squaring '''
    z = x*x
    return z
    
    
def freq(ca):     
    return {ch: ca.count(ch) for ch in ca}
    

def flatten(lst):
    res = []
    for ele in lst:
        if type(ele) is list or type(ele) is tuple:
            res += flatten(ele)
        else:
            res.append(ele)
    return res     

def mysum(lst):
        return 0 if not lst else lst[0] + mysum(lst[1:])
     
    
def mean(*lst1):
    lst = flatten(lst1)    
    return mysum(lst)/len(lst)   
    
    
def is_prime(n):
	import math	
	if n % 2 == 0:
		return False
	sqrt_n = int(math.floor(math.sqrt(n)))
	for i in range(3, sqrt_n + 1, 2):
		if n % i == 0:
			return False
	return True
    
def load(url):
    import requests
    import time
    import threading
    time.sleep(5)
    print("Starting to download ", url, 
        " from thread ", 
        threading.current_thread().getName())
    conn = requests.get(url)    
    return [url, len(conn.text)]    