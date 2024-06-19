from collections import defaultdict
record=defaultdict(int)
votes=list(map(int,input().split()))
for vote in votes:
    record[vote]+=1
a=max(record.values())
votes=set(votes)
ans=[]
for vote in votes:
    if record[vote]==a:
        ans.append(vote)
ans.sort()
print(' '.join(map(str,ans)))