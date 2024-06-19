n,a,b,c=map(int,input().split())
length=[a,b,c]
length.sort()
answer=[]
if n%length[0]==0:
    print(n//length[0])
else:
    for i in range(min(length[0],n//length[2]+1)):
        for ii in range(min(length[0],n//length[1]+1)):
            if (n-i*length[2]-ii*length[1])%length[0]==0:
                answer.append((n-i*length[2]-ii*length[1])//length[0]+i+ii)
                break
    print(max(answer))