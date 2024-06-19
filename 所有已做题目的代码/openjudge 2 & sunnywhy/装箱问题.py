deals=[]
answers=[]
while True:
    deal=input().split()
    if deal==['0','0','0','0','0','0']:
        break
    deals.append(deal)
for deal in deals:
    n1,n2,n3,n4,n5,n6=map(int,deal)
    x=n6+n5+n4+(n3-1)//4+1 #6*6，5*5，4*4每有1个就需要1个包裹，3*3每有4个就需要1个包裹
    n3=n3-n3//4*4 #3*3每4个一组处理后剩余的数量
    if n1-n5*11<=0:
        x=x #优先将1*1填入5*5的空隙，如果有多余空隙，无需处理
        if n2-n4*5<=0:
            answers.append(x) #再将2*2填入4*4的空隙，如果有多余空隙，也无需处理
        else:
            n2=n2-n4*5 #这种情况下,只剩2*2和3*3的包裹未处理
            if n3==0:
                x=x+(n2-1)//9+1
                answers.append(x)
            else:
                x=x+(n2-(-2*n3+8))//9+1
                answers.append(x) #至此，第一大类讨论完毕
    else:
        n1=n1-n5*11 #1*1填入5*5的空隙后剩余的数量
        if n2-n4*5<=0: #2*2填入4*4的空隙后仍有空隙
            n1=n1-(n4*20-n2*4) #1*1继续填入上述空隙
            if n1<=0: #剩余的1*1能全部填入
                answers.append(x) 
            else: #剩余的1*1不能全部填入
                if n3==0:
                    x=x+(n1-1)//36+1
                    answers.append(x)
                else:
                    n1=n1-9*(4-n3) #继续将1*1填入3*3的空隙
                    if n1<=0: #能全部填入
                        answers.append(x)
                    else: #不能全部填入
                        x=x+(n1-1)//36+1 #多余的1*1每有36个就再多1个包裹 
                        answers.append(x)
        else: 
             n2=n2-n4*5 #2*2填入4*4后仍有剩余，此时还有n1个1*1，n2个2*2，n3个3*3未处理
             if n3==0:
                x=x+(n2-1)//9+1 #先放2*2，每9个就再多一个包裹
                n2=n2-n2//9*9
                if n2==0:
                    x=x+(n1-1)//36+1 #2*2恰好成组，再放1*1
                    answers.append(x)
                else:
                    x=x+(n1-(-4*n2+37))//36+1 #用1*1填2*2的空隙
                    answers.append(x)
             if n3==1 and n2<=5:
                 x=x+(n1-(-4*n2+28))//36+1
                 answers.append(x)
             if n3==1 and n2>5:
                 n2=n2-5
                 n1=n1-7
                 x=x+(n1+4*n2-1)//36+1
                 answers.append(x)
             if n3==2 and n2<=3:
                 x=x+(n1-(-4*n2+19))//36+1
                 answers.append(x)
             if n3==2 and n2>3:
                 n2=n2-3
                 n1=n1-6 
                 x=x+(n1+4*n2-1)//36+1
                 answers.append(x)
             if n3==3 and n2<=1:
                 x=x+(n1-(-4*n2+10))//36+1
                 answers.append(x)
             if n3==3 and n2>1:
                 n2=n2-1 
                 n1=n1-5 
                 x=x+(n1+4*n2-1)//36+1
                 answers.append(x)
for answer in answers:
    print(answer)