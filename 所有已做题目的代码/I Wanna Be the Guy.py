n=int(input())
p=input().split()
q=input().split()
r=[]
for i in range(1,len(p)):
    r.append(int(p[i]))
for ii in range(1,len(q)):
    r.append(int(q[ii]))
s=set(r)
if len(s)>=n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
    
    