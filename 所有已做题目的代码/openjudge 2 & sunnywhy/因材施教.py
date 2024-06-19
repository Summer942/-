n,m=map(int,input().split())
grade=list(map(int,input().split()))
grade.sort()
difference=[]
for i in range(n-1):
    difference.append(grade[i+1]-grade[i])
difference.sort()
print(sum(difference[0:n-m]))
