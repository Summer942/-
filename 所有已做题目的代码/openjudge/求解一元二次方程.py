answers=[]

def formula(a,b,c):
    delta=b**2-4*a*c
    if delta>0:
        d=(-b+delta**(1/2))/(2*a)
        e=(-b-delta**(1/2))/(2*a)
        answers.append("x1="+'{:.5f}'.format(d)+";x2="+'{:.5f}'.format(e))
    elif delta==0:
        if b==0:
            b=-b
        f=-b/(2*a)
        answers.append("x1=x2="+'{:.5f}'.format(f))
    else:
        if b==0:
            b=-b
        g=(-delta)**(1/2)
        real_part=-b/(2*a)
        imaginary_part=g/(2*a)
        answers.append("x1="+'{:.5f}'.format(real_part)+'+'+'{:.5f}'.format(imaginary_part)+'i'+';x2='+'{:.5f}'.format(real_part)+'-'+'{:.5f}'.format(imaginary_part)+'i')

n=int(input())
for i in range(n): 
    x,y,z=map(float,input().split())
    formula(x,y,z)       
for answer in answers:
    print(answer)