word=input()
x=y=0
for i in word:
    if i==i.upper():
        x+=1
    else:
        y+=1
if x>y:
    print(word.upper())
else:
    print(word.lower())

