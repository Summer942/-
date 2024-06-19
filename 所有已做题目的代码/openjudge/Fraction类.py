a1,b1,a2,b2=map(int,input().split())
c1=a1*b2+a2*b1
c2=b1*b2
for i in range(c2,0,-1):
    if c1%i==0 and c2%i==0:
        c1//=i
        c2//=i
print(format(c1)+'/'+format(c2))