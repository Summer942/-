class Binheap:
    def __init__(self):
        self.heaplist=[0]
        self.currentsize=0
    def percup(self,i): #向上交换
        while i//2>0: #注意到索引为i的节点，其父节点为i//2
            if self.heaplist[i]<self.heaplist[i//2]: #小于则交换
                tmp=self.heaplist[i]
                self.heaplist[i]=self.heaplist[i//2]
                self.heaplist[i//2]=tmp
            i//=2
    def insert(self,k): #将元素放入“堆”中，然后进行向上交换使堆顶元素最小
        self.heaplist.append(k)
        self.currentsize+=1
        self.percup(self.currentsize)
    def percdown(self,i): #向下交换
        while i*2<=self.currentsize: #当前节点有子节点
            mc=self.minchild(i) 
            if self.heaplist[i]>self.heaplist[mc]:
                tmp=self.heaplist[i]
                self.heaplist[i]=self.heaplist[mc]
                self.heaplist[mc]=tmp
            i=mc
    def minchild(self,i): #获得较小子节点的索引
        if i*2+1>self.currentsize: #当前节点只有一个子节点
            return i*2
        if self.heaplist[2*i]<self.heaplist[2*i+1]: #当前节点有两个子节点，比较得到较小的那个
            return i*2
        else:
            return i*2+1
    def delmin(self): #弹出堆顶元素，然后将最后一个入堆的元素放到堆顶（保证堆的结构性质）并进行向下交换
        tmp=self.heaplist[1]
        self.heaplist[1]=self.heaplist[self.currentsize]
        self.currentsize-=1
        self.heaplist.pop()
        self.percdown(1)
        return tmp
n=int(input())
bh=Binheap()
for _ in range(n):
   input_=input().split()
   if input_[0]=='1':
        bh.insert(int(input_[1]))
   else:
       print(str(bh.delmin()))