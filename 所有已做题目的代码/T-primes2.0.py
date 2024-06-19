is_prime=[True]*1000001
primes=[]
for i in range(2,1000001):
    if is_prime[i]:
        primes.append(i)
    for j in primes:
        if j*i>1000000:
            break
        is_prime[j*i]=False
        if i%j==0:
            break
primes=set(primes)
m=int(input())
nums=list(map(int,input().split()))
for num in nums:
    if int(num**0.5)==num**0.5 and int(num**0.5) in primes:
        print('YES')
    else:
        print('NO')