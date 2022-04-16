import sys

input = sys.stdin.readline

n,s = map(int,input().split())

arr = list(map(int,input().split()))

answer = 0

def dfs(index,sum):

    global answer

    if index >= n:
        return

    sum += arr[index]

    if sum == s:
        answer +=1

    dfs(index + 1, sum) 
    dfs(index + 1, sum-arr[index])



dfs(0,0)
print(answer)