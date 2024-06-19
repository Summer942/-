def is_possible_out_stack(x,test):
    stack=[]
    x=list(x)
    if len(x)!=len(test):
        return 'NO'
    for i in test:
        while (not stack or stack[-1]!=i) and x: #当栈是空的或者当前元素不是栈顶元素时
            stack.append(x.pop(0)) #x中元素按序入栈
        if not stack or stack[-1]!=i:
            return 'NO'
        stack.pop() #当前元素为栈顶元素，出栈
    return 'YES'
x=input().strip()
while True:
    try:
        test=input().strip()
        print(is_possible_out_stack(x,test))
    except EOFError:
        break