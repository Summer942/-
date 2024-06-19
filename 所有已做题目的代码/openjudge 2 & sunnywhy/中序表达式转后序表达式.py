def middle_to_post(expression):
    priority={'+':1,'-':1,'*':2,'/':2} #定义运算优先级
    stack=[] #空栈，储存运算符号
    ans=[] #储存答案
    for i in expression:
        if i.isdigit() or '.' in i: #如果是数字，直接加入ans中
            ans.append(i)
        elif i=='(': #如果是（，直接加入stack中
            stack.append(i)
        elif i==')': #如果是），与最近的（匹配，之间的运算符号加入ans中
            while stack and stack[-1]!='(':
                ans.append(stack.pop())
            stack.pop() #将匹配的（弹出
        else: #如果是运算符号，比较当前符号与栈顶符号的优先级
            while stack and stack[-1]!='(' and priority[i]<=priority.get(stack[-1],0):
                ans.append(stack.pop())
            stack.append(i)
    while stack: #剩余符号全部弹出，加入ans
        ans.append(stack.pop())
    return ' '.join(ans)
n=int(input())
for ii in range(n):
    expression=input().replace('+', ' + ').replace('-', ' - ')\
                      .replace('*', ' * ').replace('/', ' / ')\
                      .replace('(', ' ( ').replace(')', ' ) ').split() #增加空格，便于分离 
    print(middle_to_post(expression))