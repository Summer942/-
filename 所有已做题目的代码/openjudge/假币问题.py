n=int(input())
for i in range(n):
    real={'A','B','C','D','E','F','G','H','I','J','K','L'}
    heavy=real
    light=real
    for ii in range(3):
        test=input().split()
        if test[2]=='even':
            heavy=heavy-set(test[0])-set(test[1])
            light=light-set(test[0])-set(test[1])
        elif test[2]=='up':
            heavy=heavy&set(test[0])
            light=light&set(test[1])
        else:
            heavy=heavy&set(test[1])
            light=light&set(test[0])
    if heavy:
        print(''.join(heavy)+' is the counterfeit coin and it is heavy.')
    else:
        print(''.join(light)+' is the counterfeit coin and it is light.')