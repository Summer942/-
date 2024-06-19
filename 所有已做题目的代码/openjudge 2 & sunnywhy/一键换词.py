words=input().split()
old,new=input().split()
old=old.lower()
new=new.lower()
text=[]
for i,word in enumerate(words):
    if i==0 or words[i-1][-1]=='.': #每句话的第一个词
        if word[-1]=='.' or word[-1]==',':
            a=word[-1]
            word=word[:-1].lower()
        else:
            a=''
            word=word.lower()
        if word==old:
            text.append(new.capitalize()+a)
        else:
            text.append(word.capitalize()+a)
    else:
        if word[-1]=='.' or word[-1]==',':
            a=word[-1]
            word=word[:-1].lower()
        else:
            a=''
            word=word.lower()
        if word==old:
            text.append(new+a)
        else:
            text.append(word+a)
print(' '.join(text))