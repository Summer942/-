words=input()
words=words.lower()
new=[]
for word in words:
    if word=='a' or word=='e' or word=='i' or word=='o' or word=='u' or word=='y':
        continue
    else:
        new.append(word)
print('.'+'.'.join(new))

