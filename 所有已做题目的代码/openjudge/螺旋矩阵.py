n=int(input())
answer=[[0]*n for i in range(n)]
num=1
direction=0
top=left=0
bottom=right=n-1
while top<=bottom and left<=right:
    if direction==0:
        for i in range(left,right+1):
            answer[top][i]=num
            num+=1
        top+=1
    elif direction==1:
        for ii in range(top,bottom+1):
            answer[ii][right]=num
            num+=1
        right-=1
    elif direction==2:
        for iii in range(right,left-1,-1):
            answer[bottom][iii]=num
            num+=1
        bottom-=1
    elif direction==3:
        for iiii in range(bottom,top-1,-1):
            answer[iiii][left]=num
            num+=1
        left+=1
    direction=(direction+1)%4
for _ in answer:
    print(' '.join(map(str,_)))