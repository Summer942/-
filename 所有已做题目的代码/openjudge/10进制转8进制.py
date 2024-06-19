a=int(input())
ans=[]
while a//8!=0:
    ans.insert(0,a%8)
    a=a//8
ans.insert(0,a%8)
print(''.join(map(str,ans)))
