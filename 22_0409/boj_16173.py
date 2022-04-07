import sys
from collections import deque

N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


dx = [1,0]
dy = [0,1]


def bfs(start_x,start_y):

    q = deque()
    q.append([start_x,start_y])

    visited[start_x][start_y] = True

    while q:

        x,y = q.popleft()

        if graph[x][y] == -1:
            print("HaruHaru")
            return

        jump = graph[x][y]

        for i in range(len(dx)):

            nx = x + dx[i] * jump
            ny = y + dy[i] * jump

            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True

    print('Hing')

bfs(0,0)
