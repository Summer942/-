import re
terms=re.findall(r'(\d*)n\^(\d+)',input())
a=0
for (xishu,zhishu) in terms:
    if xishu=='0':
        continue
    a=max(a,int(zhishu))
print('n^'+format(a))