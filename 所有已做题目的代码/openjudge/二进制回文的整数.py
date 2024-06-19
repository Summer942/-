n=int(input())
a=bin(n)
a=a[2:]
left=0
right=len(a)-1
flag=0
while left<right:
    if a[left]!=a[right]:
        flag=1
        print('No')
        break
    else:
        left+=1
        right-=1
if flag==0:
    print('Yes')
        
