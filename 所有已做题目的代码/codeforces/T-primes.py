def Sieve_of_Eratosthenes(x):
    numbers=[True]*(x + 1)
    numbers[0]=numbers[1]=False
    for i in range(2, int(x**0.5)+1):
        if numbers[i]:
            j=i*i
            while j <= x:
                numbers[j]=False
                j+=i
    return numbers
def is_T_prime(numbers,y):
    sqrt_y=int(y**0.5)
    if sqrt_y**2!=y:
        return False
    if numbers[sqrt_y] and sqrt_y<len(numbers):
        return True
    return False
n=int(input())
number=list(map(int,input().split()))
max_number=max(number)
numbers=Sieve_of_Eratosthenes(int(max_number**0.5)+1)
for _ in number:
    if is_T_prime(numbers, _):
        print('YES')
    else:
        print('NO')
        