word_1=input()
word_2=input()
for i in range(len(word_1)):
    if word_1[i]!=word_2[-(i+1)]:
        print('NO')
        break
    if i==len(word_1)-1:
        print('YES')