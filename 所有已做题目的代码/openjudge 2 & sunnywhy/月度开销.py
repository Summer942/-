def check(budgets,m,mid):
    count=0
    total=0
    for budget in budgets:
        total+=budget
        if total>mid:
            count+=1
            total=budget
    if total>0:
        count+=1
    return count<=m
def min_max_cost(budgets,n,m):
    left=max(budgets)
    right=sum(budgets)
    while left<right:
        mid=(left+right)//2
        if check(budgets,m,mid):
            right=mid
        else:
            left=mid+1
    return left
n,m=map(int,input().split())
budgets=[int(input())for _ in range(n)]
print(min_max_cost(budgets,n,m))