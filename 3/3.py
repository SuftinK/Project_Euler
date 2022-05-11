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
    

start = time.time()    
a = 600851475143
"""
a = 13195
answer_list = list()
for i in range(2, a):
	if isPrime(i) and a % i == 0:
		print(i)
		answer_list.append(i)

print(answer_list)
print(max(answer_list))

answer2 = [i for i in range(2, a) if a % i == 0]
print(answer2)
print(max(answer2))
"""

prime=prime_sieve_Eratosthenes(1000000000)
print(f"the list of prime numbers created. the max value is {max(prime)}")

for i in prime[::-1]:
	if a % i == 0:
		print('Answer is ', i)
		break
		
print(f"this problem realization took me {round(time.time() - start, 2)} sec.")