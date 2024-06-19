n=int(input())
for i in range(n):
    word=input()
    number=len(word)
    if number>10:
        print(word[0]+str(number-2)+word[-1])
    else:
        print(word)

