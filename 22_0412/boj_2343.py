import sys

input = sys.stdin.readline

n,m = map(int,input().split())

blay = list(map(int,input().split()))

left = max(blay)
right = sum(blay)



while left <= right:

    middle = (left + right)//2

    cnt = 0
    sum = 0

    for i in blay:
        if sum + i > middle:
            cnt+=1
            sum = 0
            
        sum += i

    if cnt >= m:
        left = middle + 1

    else:
        right = middle - 1

print(left)
