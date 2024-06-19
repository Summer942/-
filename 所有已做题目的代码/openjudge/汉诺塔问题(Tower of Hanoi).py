def hanoi(n,begin,middle,end):
    if n==1:
        print('1:'+format(begin)+'->'+format(end))
    else:
        hanoi(n-1,begin,end,middle)
        print(format(n)+':'+format(begin)+'->'+format(end))
        hanoi(n-1,middle,begin,end)
n,a,b,c=input().split()
n=int(n)
hanoi(n,a,b,c)
