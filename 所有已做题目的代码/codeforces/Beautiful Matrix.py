L1=input().split()
L2=input().split()
L3=input().split()
L4=input().split()
L5=input().split()
for i in range(0,5):
    if int(L1[i])==1:
        x=1 
        y=i+1
for j in range(0,5):
    if int(L2[j])==1:
        x=2 
        y=j+1
for k in range(0,5):
    if int(L3[k])==1:
        x=3 
        y=k+1
for l in range(0,5):
    if int(L4[l])==1:
        x=4
        y=l+1
for m in range(0,5):
    if int(L5[m])==1:
        x=5 
        y=m+1
if x>3:
    a=x-3
else:
    a=3-x
if y>3:
    b=y-3
else:
    b=3-y
c=a+b
print(c)