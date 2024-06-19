n=int(input())
groups=list(map(int,input().split()))
group_4=groups.count(4)
group_3=groups.count(3)
group_2=groups.count(2)
group_1=groups.count(1)
if group_3>=group_1:
    car=group_4+group_3+(group_2-1)//2+1
else:
    group_1=group_1-group_3
    car=group_4+group_3+(2*group_2+group_1-1)//4+1
print(car)