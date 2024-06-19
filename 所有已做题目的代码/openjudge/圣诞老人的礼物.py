n,w=map(int,input().split())
items=[]
for i in range(n):
    values,weights=map(int,input().split())
    unit_price=values/weights
    items.append([unit_price,values,weights])
items.sort(reverse=True)
value=weight=0
for ii in range(n):
    if weight+items[ii][2]<=w:
        weight+=items[ii][2]
        value+=items[ii][1]
    else:
        value+=(w-weight)*items[ii][0]
        break
print("{:.1f}".format(value))

