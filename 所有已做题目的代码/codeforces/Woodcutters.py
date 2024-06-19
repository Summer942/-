n=int(input())
trees=[list(map(int,input().split()))for i in range(n)]
number=2
for ii in range(1,n-1): 
    if trees[ii-1][0]<trees[ii][0]-trees[ii][1]:
        number+=1
    else:
        if trees[ii][0]+trees[ii][1]<trees[ii+1][0]:
            trees[ii][0]=trees[ii][0]+trees[ii][1]
            number+=1
if n==1:
    number=1
print(number)
    