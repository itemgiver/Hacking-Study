import hashlib
import sys
import time
begintime = time.time()
i = 0
tmp = "9639ac145cbfc6b16cbaafff0465260fad85f676"
while True:
    if hashlib.sha256(tmp.strip().encode('utf-8') + str(i).encode('utf-8')).hexdigest()[:6] == '0'*6:
        print(i)
        endtime = time.time()
        print('took '+str(endtime - begintime)+'s')
        break
    i += 1
