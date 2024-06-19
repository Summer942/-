def merge_sort(arr):
    n=len(arr)
    if n<=1:
        return 0
    mid=n//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    swaps=merge_sort(left_arr)+merge_sort(right_arr)
    i=j=k=0
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i]<=right_arr[j]:
            arr[k]=left_arr[i]
            i+=1
        else:
            arr[k]=right_arr[j]
            j+=1
            swaps+=(mid-i)
        k+=1
    while i<len(left_arr):
        arr[k]=left_arr[i]
        i+=1
        k+=1
    while j<len(right_arr):
        arr[k]=right_arr[j]
        j+=1
        k+=1
    return swaps
while True:
    n=int(input())
    if n==0:
        break
    arr=[]
    for _ in range(n):
        arr.append(int(input()))
    print(merge_sort(arr))