from functools import cmp_to_key
n=int(input())
numbers=input().split()
def compare(x,y):
    if x+y>y+x:
        return 1
    elif x+y==y+x:
        return 0
    else:
        return -1
numbers=sorted(numbers,key=cmp_to_key(compare))
number_min=(''.join(numbers))
number_max=(''.join(numbers[::-1]))
print(number_max,number_min)