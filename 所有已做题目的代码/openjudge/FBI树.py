class FBItree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def build_tree(string):
    if string=='1':
        return FBItree('I')
    if string=='0':
        return FBItree('B')
    if '1' in string and '0' in string:
        root=FBItree('F')
    elif '0' not in string:
        root=FBItree('I')
    else:
        root=FBItree('B')
    string1=string[:len(string)//2]
    string2=string[len(string)//2:]
    root.left=build_tree(string1)
    root.right=build_tree(string2)
    return root
def postfix(root):
    if not root:
        return ''
    result=''
    result+=postfix(root.left)
    result+=postfix(root.right)
    result+=root.val
    return result
N=int(input())
string=input()
root=build_tree(string)
result=postfix(root)
print(result)