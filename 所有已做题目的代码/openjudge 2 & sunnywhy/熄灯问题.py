import copy
light=[[0]*8,[],[],[],[],[],[0]*8]
for i in range(1,6):
    light[i]=[0]+list(map(int,input().split()))+[0]
first_steps=[]
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        first_steps.append([a,b,c,d,e,f])
for first_step in first_steps:
    light_=copy.deepcopy(light)
    answer=[['0']*6 for ii in range(5)]
    for j in range(6):
        if first_step[j]==1:
            answer[0][j]='1'
            light_[1][j+1]=abs(light_[1][j+1]-1)
            light_[1][j]=abs(light_[1][j]-1)
            light_[1][j+2]=abs(light_[1][j+2]-1)
            light_[0][j+1]=abs(light_[0][j+1]-1)
            light_[2][j+1]=abs(light_[2][j+1]-1)
    for jj in range(2,6):
        for jjj in range(1,7):
            if light_[jj-1][jjj]==1:
                answer[jj-1][jjj-1]='1'
                light_[jj][jjj]=abs(light_[jj][jjj]-1)
                light_[jj+1][jjj]=abs(light_[jj+1][jjj]-1)
                light_[jj-1][jjj]=abs(light_[jj-1][jjj]-1)
                light_[jj][jjj+1]=abs(light_[jj][jjj+1]-1)
                light_[jj][jjj-1]=abs(light_[jj][jjj-1]-1)
    if sum(light_[5][1:-1])==0:
        for _ in answer:
            print(' '.join(_))
        break