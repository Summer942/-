n=int(input())
items=[list(map(int,input().split()))for _ in range(n)]
items=sorted(items,key=lambda x:(-x[1],x[0]))
ans1=ans2=0
for i in range(n):
    ans1+=items[i][0]
    ans2=max(ans2,ans1+items[i][1])
print(ans2)

