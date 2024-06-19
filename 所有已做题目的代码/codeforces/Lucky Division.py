num=input()
for i in range(len(num)):
    if num[i]!='4' and num[i]!='7':
        if int(num)%4==0 or int(num)%7==0 or int(num)%44==0 or int(num)%47==0 or int(num)%74==0 or int(num)%77==0 or int(num)%444==0 or int(num)%447==0 or int(num)%474==0 or int(num)%744==0 or int(num)%477==0 or int(num)%747==0 or int(num)%774==0 or int(num)%777==0: 
            print('YES')
            break
        else:
            print('NO')
            break
    else:
        if i==len(num)-1:
            print('YES')
            break
        