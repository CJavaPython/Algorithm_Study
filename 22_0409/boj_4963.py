import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_x,start_y):

    q = deque()
    q.append([start_x,start_y])

    graph[start_x][start_y] = 0

    while q:

        x,y = q.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                

while True:

    count = 0

    dx = [1, -1, 0, 0, 1, -1, 1, -1] #대각선 처리를위해 상 하 좌 우 + 대각상하좌우
    dy = [0, 0, -1, 1, -1, -1, 1, 1]

    w,h = map(int,input().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int,input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i,j)  
                count += 1

    print(count)  
