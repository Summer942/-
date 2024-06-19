from collections import defaultdict
n=int(input())
models=[input().split('-')for i in range(n)]
result=defaultdict(list)
for ii in range(n):
    result[models[ii][0]].append(models[ii][1])
for model in result.keys():
    result[model]=sorted(result[model],key=lambda x:(x[-1],-float(x[0:-1])),reverse=True)
names=list(result.keys())
names.sort()
for model in names:
    print(format(model)+': '+', '.join(result[model]))            