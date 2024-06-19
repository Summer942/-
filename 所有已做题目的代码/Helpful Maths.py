formula=input().split('+')
n=len(formula)
formula.sort()
for i in range(n-1):
    formula.insert((2*i+1),'+')
print(''.join(formula))

