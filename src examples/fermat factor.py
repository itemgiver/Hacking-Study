from gmpy2 import *

def fermat_factor(n):
    a = isqrt(n)
    b2 = square(a)-n
    while not is_square(b2):
        a += 1
        b2 = square(a)-n
    p = a+isqrt(b2)
    q = a-isqrt(b2)
    
    return int(p),int(q)

n = 0x375181e744049d87f0016e9ca65b5e277a223c85074a74284f5535222c9af3bf7825838d34a7dade86d23e4f5a48fbca528259d9bf33491a024eccc9bcd2104bcee49641db3a036ebecfe6c02ffd5045d5a0a80d39836caa2836f3b0e642e62a0956b65c34e1cfab2e7f6a5c748908342e2db515c2aa51fd88f9855f364c207f3
e = 0x10001
c = 0x1dad56da6eeccae06b8196681e6c1dc651b7ad24f4c6e84daa83f9509ab367b795bf48502176b564a5e8be0c79bc015c1497dea84e558635debab18239280e27eea2d8d0cd4eb7ac3c0a41bab7c8a247139cbc1744e48b7da2b4eca931f761dded2a8c359615c0679d0425e8f2d78b6ac5eea6a1af6774d6ced960ab59f98683a

p,q = fermat_factor(n)

print(p*q == n)
