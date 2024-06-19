n=int(input())
sentence=[]
x=1
while x<=n:
    if x%2==1:
        sentence.append('that I hate')
    else:
        sentence.append('that I love')
    x+=1
sentence=' '.join(sentence).split()
del sentence[0]
sentence.append('it')
print(' '.join(sentence))