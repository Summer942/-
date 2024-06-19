n,m=map(int,input().split())
array=input().split()
array_new=set()
for i in range(n):
    array_new.add(array[n-i-1])
    array[n-i-1]=len(array_new)
for ii in range(m):
    l=int(input())
    print(array[l-1])
    
    