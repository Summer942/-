is_prime=[True]*(10001)
primes=[]
for i in range(2,10001):
    if is_prime[i]:
        primes.append(i)
    for j in range(len(primes)):
        if primes[j]*i>10000:
            break
        is_prime[primes[j]*i]=False
        if i%primes[j]==0:
            break
primes=set(primes)
sum_=int(input())
if sum_%2!=0:
    A=2
    B=sum_-A
else:
    for prime in primes:
        if sum_-prime in primes:
            A=prime
            B=sum_-prime
            break
print(A,B)