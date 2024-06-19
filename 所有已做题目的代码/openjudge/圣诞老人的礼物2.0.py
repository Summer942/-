N,W=map(int,input().split())
candies=[]
ans=0
for i in range(N):
    v,w=map(int,input().split())
    v_average=v/w
    candies.append([v/w,w,v])
candies.sort(reverse=True)
for [a,b,c] in candies:
    if b<=W:
        ans+=c
        W-=b
    else:
        ans+=a*W
        break
print("{:.1f}".format(ans))