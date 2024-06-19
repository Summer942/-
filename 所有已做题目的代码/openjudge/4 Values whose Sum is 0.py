from collections import defaultdict
n=int(input())
A,B,C,D=[],[],[],[]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
A_plus_B=defaultdict(int)
for a in A:
    for b in B:
        A_plus_B[a+b]+=1
count=0
for c in C:
    for d in D:
        if -(c+d) in A_plus_B:
            count+=A_plus_B[-(c+d)]
print(count)