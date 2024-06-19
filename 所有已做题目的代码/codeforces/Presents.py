n=int(input())
friends=input().split()
friend=[]
for i in range(n):
    a=friends.index(str(i+1))
    friend.append(str(a+1))
print(' '.join(friend))