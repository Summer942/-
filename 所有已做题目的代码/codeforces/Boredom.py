n=int(input())
sequence=list(map(int,input().split()))
dp=[0]*100001
for i in sequence:
    dp[i]+=i
a=b=0
for j in dp:
    a,b=max(b+j,a),a
print(a)