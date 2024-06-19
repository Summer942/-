s=input().split()
n=int(s[0])
h=int(s[1])
p=input().split()
x=0
for i in range(n):
    if int(p[i])<=h:
        x+=1
    else:
        x+=2
print(x)
    