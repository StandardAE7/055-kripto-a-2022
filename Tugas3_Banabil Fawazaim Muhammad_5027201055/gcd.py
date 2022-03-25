def gcd(a,b):
    if(a < b):
        temp = a
        a = b
        b = temp
    if(b == 0):
        return a
    else:
        return gcd(b, a%b)

print(gcd(66528,52920))