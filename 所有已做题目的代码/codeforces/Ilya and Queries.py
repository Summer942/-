s=input()
answer=[0]*len(s)
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        answer[i]=answer[i-1]+1
    else:
        answer[i]=answer[i-1]
m=int(input())
for ii in range(m):
    l,r=map(int,input().split())
    print(answer[r-1]-answer[l-1])