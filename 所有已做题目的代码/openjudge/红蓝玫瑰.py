roses=list(input())
n=len(roses)
R=[0]*n
B=[0]*n
if roses[0]=='R':
    R[0]=0
    B[0]=1
else:
    R[0]=1
    B[0]=0
for i in range(n-1):
    if roses[i+1]=='R':
        R[i+1]=R[i]
        B[i+1]=min(B[i],R[i])+1
    else:
        B[i+1]=B[i]
        R[i+1]=min(B[i],R[i])+1
print(R[-1])
        