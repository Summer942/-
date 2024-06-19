A,B,K=map(int,input().split()) #读取输入
field=[[1]*(B) for i in range(A)] #列表推导式形成棋盘
m=1 #记录pillbox可能位置对应的值
for ii in range(K):
    R,S,P,T=map(int,input().split())
    if T==1: #炸到了，将炸弹范围内的数乘以2，并更新m，注意炸弹范围是否越界
        for j in range(max(0,R-1-(P-1)//2),min(A,R+(P-1)//2)):
            for k in range(max(0,S-1-(P-1)//2),min(B,S+(P-1)//2)):
                field[j][k]=field[j][k]*2
        m=m*2
    else: #没炸到，将炸弹范围内的数标记为0，由于0乘以任何数还为0，可彻底排除
        for j in range(max(0,R-1-(P-1)//2),min(A,R+(P-1)//2)):
            for k in range(max(0,S-1-(P-1)//2),min(B,S+(P-1)//2)):
                field[j][k]=0
n=0 #记录位置个数
for iii in range(A):
    n+=field[iii].count(m)
print(n)
                
    