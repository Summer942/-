from math import sqrt
test=0
while True:
    n,d=map(int,input().split())
    if n==d==0:
        break
    else:
        test+=1
        area=[]
        for i in range(n):
            x,y=map(int,input().split())
            if d>=y:
                area.append([x-sqrt(d**2-y**2),x+sqrt(d**2-y**2)])
        input()
        if len(area)<n:
            print('Case {}: -1'.format(test))
        else:
            area.sort(reverse=True)
            num=n
            z=area[0][0]
            for ii in range(1,n):
                if area[ii][1]<z:
                    z=area[ii][0]
                else:
                    num-=1
            print('Case {}: {}'.format(test,num))