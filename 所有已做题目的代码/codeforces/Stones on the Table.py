C={'R':1,'G':2,'B':3}
n=int(input())
color=input()
times=0
for i in range(n-1):
    if C[color[i]]==C[color[i+1]]:
        times=times+1
    else:
        times=times
print(times)

