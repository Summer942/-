def sieve_of_eratosthenes(x):
    numbers=[True]*(x+1)
    numbers[0]=numbers[1]=False
    for i in range(2,int(x**0.5)+1):
        if numbers[i]:
            j=i*i
            while j<=x:
                numbers[j]=False
                j+=i 
    for ii in range(3,x//2+1): 
        if numbers[ii] and numbers[x-ii]: 
            print(f'{x}'+'='+f'{ii}'+'+'+f'{x-ii}')
x=int(input())
if x%2!=0 or x<6:
    print('Error!')
else:
    sieve_of_eratosthenes(x)