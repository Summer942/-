def eulersieve(n):
    is_prime=[True]*(n+1)
    primes=[]
    for i in range(2,n+1):
        if is_prime[i]:
            primes.append(i)
        for j in range(len(primes)):
            if primes[j]*i>n:
                break
            is_prime[primes[j]*i]=False
            if i%primes[j]==0:
                break
    return primes
n=int(input())
primes=eulersieve(n)
count={}
while n>1:
    for prime in primes:
        if n%prime==0:
            n=n//prime
            count[prime]=count.get(prime,0)+1
a=sum(count.values())
if a%2==0:
    x=1
else:
    x=-1
for value in count.values():
    if value>=2:
        x=0
print(x)
