def isPrime(n):
    return n > 1 and all(n % x != 0 for x in range(2, int(n**0.5) + 1))

def f(n):
    a = []
    for i in range(1,n+1):
        if isPrime(i) == 1:
            a.append(i)
    return a

m = int(input())



'''def prost(n):
    d = set()
    for z in range(2,n**0.5):
        if n%z==0:
            d.add(n)
            d.add(n//z)
    d = sorted()
    return d
m = int(input())
def morsen():
    if ((m-1)**0.5)*1 == int((m-1)**0.5)'''