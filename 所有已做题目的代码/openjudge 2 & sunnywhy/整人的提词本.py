from collections import deque
s=input()
stack=[]
queue=deque([])
for char in s:
    if char!=')':
        stack.append(char)
    else:
        while stack[-1]!='(':
            queue.append(stack.pop())
        stack.pop()
        while queue:
            stack.append(queue.popleft())
print(''.join(stack))