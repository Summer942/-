def prefix_to_postfix(prefix):
    if not prefix:
        return []
    root=prefix[0]
    left_prefix=[i for i in prefix if i<root]
    right_prefix=[j for j in prefix if j>root]
    return prefix_to_postfix(left_prefix)+prefix_to_postfix(right_prefix)+[root]
n=int(input())
prefix=list(map(int,input().split()))
postfix=prefix_to_postfix(prefix)
print(' '.join(map(str,postfix)))            