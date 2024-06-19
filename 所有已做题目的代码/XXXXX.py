t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    array=input().split()
    array_1=[int(a) for a in array]
    array_2=array_1.copy()
    if sum(array_1)%x!=0:
        print(n)
    else:
        for ii in range(n):
            if array_1[ii]%x!=0 or array_2[-(ii+1)]%x!=0:
                print(n-ii-1)
                break
            else:
                if ii==n-1:
                    print(-1)
                    
            