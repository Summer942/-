stack=[]
min_stack=[]
while True:
    try:
        command=input().split()
        if command[0]=='push':
            pig=int(command[1])
            stack.append(pig)
            if not min_stack:
                min_stack.append(pig)
            else:
                min_stack.append(min(pig,min_stack[-1]))
        elif command[0]=='pop':
            if stack:
                stack.pop()
                min_stack.pop()
        else:
            if min_stack:
                print(min_stack[-1])
    except EOFError:
        break