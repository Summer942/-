#经画图分析，在程序的第奇数个时刻的下一个时刻插入（如果可以的话）有可能增加亮灯时间
n,M=map(int,input().split())
program=[0]+list(map(int,input().split()))+[M]
total=on_before=ans=0
for i in range(0,n+1,2):
    total+=program[i+1]-program[i] #不插入时的总亮灯时间
ans=total
for ii in range(1,n+1,2):
    on_before+=program[ii]-program[ii-1] #插入时刻之前的亮灯时间
    if program[ii+1]>program[ii]+1: #判断能否插入
        change=total-on_before #插入时刻之后的原亮灯时间变为灭灯时间
        ans=max(ans,M-(program[ii]-on_before)-change-1) 
        # M为总时间，program[i]-on_before为插入时刻之前的灭灯时间
print(ans)