n=int(input())
juice=input().split()
x=0
for i in range(n):
 x=x+int(juice[i])/100
y=x/n*100
print(y)  