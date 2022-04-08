import sys
from collections import deque
sys.setrecursionlimit(10000)

input = sys.stdin.readline


def bfs(i,j):
    
    q = deque()
    q.append((i,j))

    graph[i][j] = 0

    while q:

        x,y = q.popleft()


        for i in range(len(dx)):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = 0

def dfs(x,y):

    graph[x][y] = 0

    for i in range(len(dx)):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                dfs(nx,ny)


while True:

    w,h = map(int,input().split())

    count = 0

    if w == 0 and h == 0:
        break

    graph = [list(map(int,input().split())) for _ in range(h)]

    dx = [1,0,-1,0,1,-1,1,-1]
    dy = [0,1,0,-1,1,1,-1,-1]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i,j)
                #bfs(i,j)
                count += 1

    print(count)

