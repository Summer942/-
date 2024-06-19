n=int(input())
x=0
for i in range(n):
    c=input()
    if c[1]=='+':
        x=x+1
    else:
        x=x-1
print(x)