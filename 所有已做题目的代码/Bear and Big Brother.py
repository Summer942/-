number=input().split()
x=int(number[0])
y=int(number[1])
z=0
while x<=y:
    x=x*3
    y=y*2
    z=z+1
print(z)