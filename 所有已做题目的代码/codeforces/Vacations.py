n=int(input())
days=list(map(int,input().split()))
rest=0
x=0
for i in range(n):
    if days[i]==0 or days[i]==x:
        rest+=1
        x=0
    elif days[i]==3:
        if x!=0: 
            x=3-x
    else:
        x=days[i]
print(rest)