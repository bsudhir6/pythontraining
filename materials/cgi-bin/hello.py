#http://localhost:8080/cgi-bin/hello.py
print("Content-Type: text/html")
print()
prefix = "<html><body>"
suffix = "</body></html>"

import os
dct = os.environ
tbldctprefix="<table border=1>"
dcttpls= dct.items()
strtabledata="";
for e in dcttpls:
    strtabledata+="<tr><td>" + e[0] + "</td><td>" + e[-1] + "</td></tr>"
tbldctsuffix="</table>"

print(prefix)
print(tbldctprefix)
print(strtabledata)
print(tbldctsuffix)
print(suffix)
