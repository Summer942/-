import heapq
class Treenode:
    def __init__(self,freq,char):
        self.freq=freq
        self.char=char
        self.left=None
        self.right=None
    def __lt__(self,other):
        if self.freq==other.freq:
            return self.char<other.char
        return self.freq<other.freq
def build_huffman_tree(freq_dict):
    heap=[Treenode(freq,char) for char,freq in freq_dict.items()]
    heapq.heapify(heap)
    while len(heap)>1:
        left=heapq.heappop(heap)
        right=heapq.heappop(heap)
        new_node=Treenode(left.freq+right.freq,left.char+right.char)
        new_node.left=left
        new_node.right=right
        heapq.heappush(heap,new_node)
    return heap[0]
def generate_huffman_code(root,code,codes_dict):
    if root:
        if len(root.char)==1:
            codes_dict[root.char]=code
        generate_huffman_code(root.left,code+'0',codes_dict)
        generate_huffman_code(root.right,code+'1',codes_dict)
freq_dict={}
n=int(input())
for _ in range(n):
    char,freq=input().split()
    freq_dict[char]=int(freq)
root=build_huffman_tree(freq_dict)
codes_dict={}
generate_huffman_code(root,'',codes_dict)
while True:
    try:
        s=input()
        if s.isdigit():
            decode=''
            current=''
            for bit in s:
                current+=bit
                if current in codes_dict.values():
                    decode+=list(codes_dict.keys())[list(codes_dict.values()).index(current)]
                    current=''
            print(decode)        
        else:
            encode=[codes_dict[bit] for bit in s]
            print(''.join(encode))
    except EOFError:
        break