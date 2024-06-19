n1=input()
n2=input()
answer=[]
for i in range(len(n1)):
    if int(n1[i])==int(n2[i]):
        answer.append('0')
    else:
        answer.append('1')
print(''.join(answer))
    