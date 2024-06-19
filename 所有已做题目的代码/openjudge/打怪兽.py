N=int(input())
for i in range(N):
    n,m,b=map(int,input().split())
    skills=[list(map(int,input().split())) for ii in range(n)]
    skills.sort(key=lambda x:x[1],reverse=True)
    times=set()
    for skill in skills:
        times.add(skill[0])
    times=list(times)
    hurt={}
    rounds={}
    for time in times:
        hurt[time]=0
        rounds[time]=0
    for skill in skills:
        if rounds[skill[0]]<m:
            hurt[skill[0]]+=skill[1]
            rounds[skill[0]]+=1 
    for time in sorted(times):
        if hurt[time]>=b:
            b-=hurt[time]
            print(time)
            break
        else:
            b-=hurt[time]
    if b>0:
        print('alive')