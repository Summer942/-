N=int(input())
camera=list(map(int,input().split()))
monitoring_area=[]
for i in range(N):
    monitoring_area.append([max(0,i-camera[i]),min(N-1,i+camera[i])])
monitoring_area.sort()
right1=right2=i=ans=0
while right1<N and i<N:
    while i<N and monitoring_area[i][0]<=right1:
        right2=max(right2,monitoring_area[i][1]+1)
        i+=1
    right1=right2
    ans+=1
print(ans)