for i in range(int(input())):
    n=int(input())
    al=sorted(list(map(int,input().split())))
    max_edge=n//2
    for i in range(n-1):
        if al[i]!=al[i+1]:
            max_edge=max(max_edge,(i+1)*(n-i-1))
    print(max_edge)
    
    