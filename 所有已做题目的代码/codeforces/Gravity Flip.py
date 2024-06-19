n=int(input())
box1=input().split()
box2=[]
box3=[]
for i in range(n):
    x=int(box1[i])
    box2.append(x)
box2.sort()
for i in range(n):
    y=str(box2[i])
    box3.append(y)
print(' '.join(box3))
