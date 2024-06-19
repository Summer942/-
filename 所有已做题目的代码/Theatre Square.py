number=input().split()
n=int(number[0])
m=int(number[1])
a=int(number[2])
if n%a==0:
    x=n//a
else:
    x=n//a+1
if m%a==0:
    y=m//a
else:
    y=m//a+1
z=x*y
print(z)


