import re
terms=re.findall(r'(\d*)n\^(\d+)',input())
zhishu=[]
for i in range(len(terms)):
    zhishu.append([int(terms[i][1]),i])
zhishu.sort(reverse=True)
x=0
a=zhishu[x][1]
while terms[a][0]=='0':
    x+=1
    a=zhishu[x][1]
print('n^'+f'{terms[zhishu[x][1]][1]}')
