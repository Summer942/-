n=input()
length=len(n)
if length<=6:
    print('NO')
for i in range(length-6):
 if int(n[i])==int(n[i+1])==int(n[i+2])==int(n[i+3])==int(n[i+4])==int(n[i+5])==int(n[i+6]):
    print('YES')
    break
 else:
     if i==length-7:
         print('NO')
         break