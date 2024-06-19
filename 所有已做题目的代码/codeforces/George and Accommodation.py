n=int(input())
x=0
for i in range(n):
    room=input().split()
    p=int(room[0])
    q=int(room[1])
    if q-p>=2:
        x+=1
    else:
        x=x 
print(x)