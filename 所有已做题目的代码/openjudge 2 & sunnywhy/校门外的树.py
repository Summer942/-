L,M=map(int,input().split())
trees=[1]*(L+1)
for _ in range(M):
    a,b=map(int,input().split())
    trees[a:b+1]=[0]*(b-a+1)
print(sum(trees))

