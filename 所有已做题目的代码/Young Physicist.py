n=int(input())
a,b,c=0,0,0
for i in range(n):
    vectors=input().split()
    x=int(vectors[0])
    y=int(vectors[1])
    z=int(vectors[2])
    a=a+x
    b=b+y
    c=c+z
if a==0 and b==0 and c==0:
    print('YES')
else:
    print('NO')