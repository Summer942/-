t=int(input())
answers=[]
for i in range(t): 
    n=int(input())
    delivery_time=list(map(int,input().split()))
    pick_up_time=list(map(int,input().split()))
    restaurants=sorted(list(zip(delivery_time,pick_up_time)),reverse=True)
    if n==1:
        answers.append(min(delivery_time[0],pick_up_time[0]))
    else:
        pick_up=0
        for ii in range(n):
            pick_up+=restaurants[ii][1]
            if pick_up>restaurants[ii][0]: 
                answers.append(max(pick_up-restaurants[ii][1],restaurants[ii][0]))
                break
            if pick_up<=restaurants[ii][0] and ii==n-1:
                answers.append(pick_up)
print('\n'.join(map(str,answers)))
    