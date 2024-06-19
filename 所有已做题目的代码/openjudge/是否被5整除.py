A=input()
ans=''
for i in range(len(A)):
    num=int(A[:i+1],2)
    if num%5==0:
        ans+='1'
    else:
        ans+='0'
print(ans)
