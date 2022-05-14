import time

start = time.time()

def prime_sieve_Eratosthenes(N):

    A=[True]*N
    primelist=[]
    A[0]=A[1]=False
    for k in range(2,N):
        if A[k]:
            for m in range(2*k,N,k):
                A[m]=False
    for k in range(N):
        if A[k]:
            primelist.append(k)
    return primelist


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def isitPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
            if k%i==0:
            	return False

    return True
n = 10001
prime=prime_sieve_Eratosthenes(1000000)
print(f"the answer is {prime[n-1]}")

print(f"this problem realization took me {round(time.time() - start, 2)} sec.")