num=input().split()
k=int(num[0])
n=int(num[1])
w=int(num[2])
money=int(k*w*(w+1)/2)
if money>n:
    x=money-n
else:
    x=0
print(x)