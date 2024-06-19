H,L,n=map(int,input().split())
speeds=list(map(int,input().split()))
speeds.sort(reverse=True)
speed=speeds[(n-1)//2]
time=L/speed
h=H-5*time**2
print('{:.2f}'.format(h))