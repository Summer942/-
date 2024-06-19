n=int(input())
ribbons=list(map(int,input().split()))
a,b={},{} #字典a用于记录每个数字出现的次数，字典b用于从第一个数到当前，所有出现次数的重复次数
ans=1
for i in range(n):
    x=ribbons[i]
    a[x]=a.get(x,0)+1 #x每出现一次，x对应的值加1
    b[a[x]]=b.get(a[x],0)+1 #a[x]每出现一次，a[x]对应的值加1
    if a[x]*b[a[x]]==i+1 and i!=n-1: #若前i+1个数恰好是b[a[x]]组数且每组数中出现次数为a[x]
        ans=i+2 #最长streak就是前i+1个数再加1
    elif a[x]*b[a[x]]==i: #若前i+1个数除去某个数之后是b[a[x]]组数且每组数中出现次数为a[x]
        ans=i+1
print(ans)