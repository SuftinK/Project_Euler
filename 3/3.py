"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import time

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

#prime=prime_sieve_Eratosthenes(100000)
#prime.remove(2)
#print(prime[:100])

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
print(isitPrime(13))

start = time.time()    
a = 600851475143

#a = 13195


answer2 = (i for i in range(a // 2, 2, -1) if a % i == 0)
print(type(answer2))
#print(max(answer2))
temp = 0
count = 1
for i_elem in answer2:
    print(count, i_elem)
    if i_elem > temp and isitPrime(i_elem):
        temp = i_elem
    count += 1

print(temp)

print(f"this problem realization took me {round(time.time() - start, 2)} sec.")