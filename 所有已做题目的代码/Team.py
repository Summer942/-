n=int(input())
number=0
for i in range(n):
    x=0
    word=input()
    for ii in range(0,5):
        if word[ii]=="1":
            x=x+1
    if x>1:
        number=number+1
print(number)