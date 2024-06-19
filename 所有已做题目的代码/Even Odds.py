number=input().split()
n=int(number[0])
k=int(number[1])
if n%2==0:
    if k<=n//2:
        x=2*k-1
    else:
        x=2*k-n
else:
    if k<=(n+1)//2:
        x=2*k-1
    else:
        x=2*k-n-1
print(x)

    
    