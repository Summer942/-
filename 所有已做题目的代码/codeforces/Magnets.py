
n=int(input())
magnets=[]
for i in range(n):
    magnet=input()
    magnets.append(magnet)
x=1
for i in range(n-1):
    if magnets[i]==magnets[i+1]:
        x=x
    else:
        x+=1
print(x)