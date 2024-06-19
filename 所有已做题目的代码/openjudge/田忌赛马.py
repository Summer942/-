while True:
    n=int(input())
    if n==0:
        break
    tian_horses=list(map(int,input().split()))
    king_horses=list(map(int,input().split()))
    tian_horses.sort(reverse=True)
    king_horses.sort(reverse=True)
    win=0
    for i in range(n):
        if tian_horses[0]>king_horses[0]:
            win+=1
            del tian_horses[0]
            del king_horses[0]
        else:
            if tian_horses[-1]>king_horses[-1]:
                win+=1
                del tian_horses[-1]
                del king_horses[-1]
            else:
                if tian_horses[-1]<king_horses[0]:
                    win-=1
                    del tian_horses[-1]
                    del king_horses[0]
    print(win*200)