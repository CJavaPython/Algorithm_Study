import sys

input = sys.stdin.readline

k,n = map(int,input().split())

lan_list = []

for i in range(k):
    lan_list.append(int(input()))

lan_list.sort()

left = 1
right = lan_list[-1]

while left <= right:

    middle = (left + right)//2
    answer = 0

    for i in lan_list:
        answer += i // middle

    if answer >= n:
        left = middle + 1

    else:
        right = middle - 1

print(right)

