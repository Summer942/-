ans=[]
def dfs(result=[],i=0,selected_row=[],diagnol_1=set(),diagnol_2=set()):
# result用于记录结果，i为行指标，selected_row为已占用的列指标，diagonal_1、2为已占用的斜线
    if i==8: #结束调用函数
       ans.append(result)
       return
    for j in range(8):
        if j not in selected_row and i+j not in diagnol_1 and i-j not in diagnol_2:
            dfs(result+[j+1],i+1,selected_row+[j],diagnol_1|{i+j},diagnol_2|{i-j})
dfs()
for _ in range(int(input())):
    index=int(input())
    print(''.join(map(str,ans[index-1])))