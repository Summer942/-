s=input().split()
n=int(s[0])
t=int(s[1])
q=input()
for i in range(t):
    q=q.replace('BG','GB',n)
print(q)