class Node:
    def __init__(self):
        self.children={} #当前节点的子节点字典
class Trie:
    def __init__(self):
        self.root=Node() #Trie的根节点为空
    def insert(self,phone_number): #添加新子树
        node=self.root
        for num in phone_number:
            if num not in node.children: #当前数字不在子节点字典中，则添加
                node.children[num]=Node()
            node=node.children[num]
    def startwith(self,prefix):
        node=self.root
        for num in prefix:
            if num not in node.children: #当前数字没有在子节点字典中出现，则不是前缀
                return False
            node=node.children[num]
        return True
for _ in range(t:=int(input())):
    n=int(input())
    phone_numbers=[input() for _ in range(n)]
    phone_numbers.sort(reverse=True) #前缀相同时，更短的后进入字典树
    trie=Trie()
    for phone_number in phone_numbers:
        flag=trie.startwith(phone_number)
        trie.insert(phone_number)
        ans='YES'
        if flag:
            ans='NO'
            break
    print(ans)