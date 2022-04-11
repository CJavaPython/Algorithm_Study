import sys

input = sys.stdin.readline

n = int(input())


left = 0
right = n


while left <= right:

    middle = (left+right) // 2

    if middle**2 < n:
        left = middle + 1

    else:
        right = middle - 1

print(left)


