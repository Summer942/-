string=list(input().lower())
for i in range(len(string)):
    if string[i]=='a'or string[i]=='e'or string[i]=='i'or string[i]=='o'or string[i]=='u'or string[i]=='y': 
       string[i]=''
string_1=''.join(string)
string_2='.'.join(list(string_1))
print('.'+string_2)
 