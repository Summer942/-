t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    array=list(map(int,input().split()))
    if sum(array)%x!=0:
        print(n)
    else:
        for ii in range(n):
            if array[ii]%x!=0 or array[-ii-1]%x!=0:
                print(n-ii-1)
                break
            else:
                if ii==n-1:
                    print(-1)