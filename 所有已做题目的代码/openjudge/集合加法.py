n=int(input())
ans=[]
for _ in range(n): 
    s=int(input())
    a=int(input())
    A_elements=list(map(int,input().split()))
    b=int(input())
    B_elements=list(map(int,input().split()))
    num=0
    hash_table={}
    for i in A_elements:
        hash_table[i]=hash_table.get(i,0)+1
    for ii in B_elements: 
        element=s-ii
        if element in hash_table:
            num+=hash_table[element]
    ans.append(num)
for iii in ans:
    print(iii)