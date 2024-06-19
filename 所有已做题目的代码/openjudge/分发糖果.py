n=int(input())
ratings=list(map(int,input().split()))
candies=[1]+[0]*(n-1)
for i in range(1,n):
    if ratings[i]>ratings[i-1]:
        candies[i]=candies[i-1]+1
    elif ratings[i]==ratings[i-1]:
        candies[i]=1
    else:
        candies[i]=1
for ii in range(n-1,0,-1):
    if ratings[ii]<ratings[ii-1]:
        if candies[ii]>=candies[ii-1]:
            candies[ii-1]=candies[ii]+1
print(sum(candies))