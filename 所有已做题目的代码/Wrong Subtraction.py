number=input().split()
n=number[0]
k=int(number[1])
x=0
while x<=k-1:
 if int(n[-1])==0:
    n=str(int(n)//10)
    x=x+1
 else:
    n=str(int(n)-1)
    x=x+1
print(int(n))