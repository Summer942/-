n=int(input())
array=list(map(int,input().split()))
total=sum(array)
if total%3!=0:
    print(0)
else:
    total_=count=answer=0
    for i in range(n-1):
        total_+=array[i]
        if total_==total//3*2:
            answer+=count
        if total_==total//3:
            count+=1
    print(answer)