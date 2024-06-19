n=input().split()
p=int(n[0])
w=int(n[1])
g=input().split()
x=0
while int(g[x])>0:
    if x==p-1:
       x=p
       break
    else:
     x=x+1
if x>w:
    while int(g[w-1])==int(g[w]):
     if w==p-1:
        w=p
        break
     else:
        w=w+1
    x=w    
else:
    x=x
print(x)


