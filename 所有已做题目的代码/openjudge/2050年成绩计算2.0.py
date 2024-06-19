is_prime=[True]*10001
primes=[]
for i in range(2,10001):
    if is_prime[i]:
        primes.append(i)
    for j in primes:
        if j*i>10000:
            break
        is_prime[j*i]=False
        if i%j==0:
            break
primes=set(primes)
m,n=map(int,input().split())
ans=[]
for k in range(m):
    grades=list(map(int,input().split()))
    total=0
    for grade in grades:
        if int(grade**0.5)==grade**0.5 and int(grade**0.5) in primes:
            total+=grade
    if total==0:
        ans.append(0)
    else:    
        ans.append("{:.2f}".format(total/len(grades)))
for _ in ans:
    print(_)