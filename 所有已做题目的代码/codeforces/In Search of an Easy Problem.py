n=int(input())
answers=[]
answer=input().split()
s=0
for i in range(n):
    x=int(answer[i])
    s=s+x
if s==0:
    print('EASY')
else:
    print('HARD')