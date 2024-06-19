n=int(input())
c=[]
d=0
for i in range(n):
    p=input().split()
    a=int(p[0])
    b=int(p[1])
    d=d-a
    c.append(d)
    d=d+b
    c.append(d)
print(max(c))