pos=-1
def exp():
    global pos
    pos+=1
    a=string[pos]
    if a=='+':
        return exp()+exp()
    if a=='-':
        return exp()-exp()
    if a=='*':
        return exp()*exp()
    if a=='/':
        return exp()/exp()
    else:
        return float(a)
string=input().split()
result=exp()
print("{:.6f}".format(result))