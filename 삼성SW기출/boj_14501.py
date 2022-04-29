import sys

input = sys.stdin.readline

n = int(input())

Ti = list()
Pi = list()

answer = 0
dp = [0] * (n+1)

for _ in range(n):

    a,b = map(int,input().split())

    Ti.append(a)
    Pi.append(b)


for i in range(n):

    answer = max(answer, dp[i])

    if i + Ti[i] > n:
        continue

    dp[i+Ti[i]] = max(answer+Pi[i],dp[i+Ti[i]])


print(max(dp))

