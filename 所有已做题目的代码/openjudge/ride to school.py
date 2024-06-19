import math
while True:
    N=int(input())
    if N==0:
        break
    time=[]
    for i in range(N):
        v,t=map(int,input().split())
        if t<0:
            continue
        time.append(t+(4.5/v)*3600)
    print(math.ceil(min(time)))
        
        