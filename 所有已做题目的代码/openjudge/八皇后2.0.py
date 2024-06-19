ans=[]
def dfs(result='',i=0,selected_row=[],diagnol_1=set(),diagnol_2=set()):
    if i==8:
        ans.append(result)
        return
    for j in range(1,9):
        if j not in selected_row and i+j not in diagnol_1 and i-j not in diagnol_2:
            dfs(result+str(j),i+1,selected_row+[j],diagnol_1|{i+j},diagnol_2|{i-j})
dfs()
for _ in range(int(input())):
    index=int(input())
    print(ans[index-1])