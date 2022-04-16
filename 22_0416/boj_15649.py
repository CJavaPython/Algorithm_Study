import sys

input = sys.stdin.readline

n,m = map(int,input().split())

visited = [False] * (n+1)
answer = list()

def dfs(depth):

    if depth == m:
        print(*answer)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(i+1)
            dfs(len(answer))
            answer.pop()
            visited[i] = False

def dfs2(depth):

    if depth == m:
        print(*answer)

    for i in range(1,n+1):
        if i not in answer:
            answer.append(i)
            dfs2(depth + 1)
            answer.pop()

dfs2(0)






