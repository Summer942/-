year=str(int(input())+1)
a,b,c,d=year[0],year[1],year[2],year[3]
while a==b or a==c or a==d or b==c or b==d or c==d:
    year=int(year)+1
    year=str(year)
    a,b,c,d=year[0],year[1],year[2],year[3]
print(year)
