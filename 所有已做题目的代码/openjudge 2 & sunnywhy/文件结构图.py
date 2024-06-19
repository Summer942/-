class root:
    def __init__(self,name):
        self.name=name
        self.dir=[]
        self.file=[]
    def build(self,s):
        if s[0]=='f': #如果root下是文件，则加入root.file中
            self.file.append(s)
        elif s[0]=='d': #如果root下是目录，则加入root.dir中，同时把目录作为新的root
            dir_=root(s)
            self.dir.append(dir_)
            while True: #在新root下重复上述过程，遇到]即停止该轮操作
                s=input()
                if s==']':
                    break
                dir_.build(s)
def graph(r,i=0): #生成“图”，r表示当前目录/根，i表示层数
    print('|     '*i+r.name)
    if r.dir: #如果有子目录，则进入下一层，重复上述操作
        for a in r.dir:
            graph(a,i+1)
    r.file.sort() #按字母表顺序排好序
    for b in r.file:
        print('|     '*i+b)
j=0 #记录测试数据的编号
while True:
    s=input()
    if s=='#': #结束接收数据
        break
    j+=1 
    r=root('ROOT') #初始的ROOT
    while True:
        r.build(s) #生成“树”
        s=input()
        if s=='*': #一组测试数据结束
            break
    print(f'DATA SET {j}:')
    graph(r,0)
    print()