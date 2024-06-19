n,k=map(int,input().split())
crows=list(map(int,input().split()))
seat_2=n*2 #2连座的数目
seat_4=n #4连座的数目
for i in range(k):
    a=crows[i]//4 #让每窝乌鸦4个1组的组数
    b=min(a,seat_4) #当前状态下能消耗的4连座数目
    seat_4-=b
    crows[i]-=(b*4) #每窝乌鸦消耗4连座后的剩余乌鸦数
seat_2+=seat_4 #4连座不可当成2个2连座，先当成1个2连座
for j in range(k):
    a=crows[j]//2 #让每窝乌鸦2个1组的组数
    b=min(a,seat_2) #当前状态下能消耗的2连座数目
    seat_2-=b
    crows[j]-=(b*2) #每窝乌鸦消耗2连座后的剩余乌鸦数
#此时若能坐飞机，则每窝乌鸦最多剩1只，若有超过2只，证明2连座已提前分完
#由于最多只剩1只乌鸦,此时的4连座可以看成2个2连座(aa空b即可),则总2连坐数目为seat_2+seat_4
if (seat_2+seat_4)>=sum(crows):
    print('YES')
else:
    print('NO')