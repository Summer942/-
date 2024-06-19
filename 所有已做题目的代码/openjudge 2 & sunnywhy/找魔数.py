square=[]
for i in range(1,33):
    square.append(i*i)
m=int(input())
numbers=list(map(int,input().split()))
for number in numbers:
    for ii in range(len(square)):
        if number-square[ii] in square:
            print(bin(number),oct(number),hex(number)) 
            break