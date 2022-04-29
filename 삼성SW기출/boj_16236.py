import sys
from collections import deque

input = sys.stdin.readline



n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

shark_size = 2

time,eat = 0,0

start_x,start_y = 0,0

for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] == 9:
            start_x,start_y = i,j

graph[start_x][start_y] = 0

while True:

    q = deque()
    q.append((start_x, start_y, 0))

    visited = [[False] * n for _ in range(n)]

    flag = float('inf')
    fish = []

    while q:

        x, y, count = q.popleft()

        if count > flag:
            print('break')
            break

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] > shark_size or visited[nx][ny]:
                continue

            if graph[nx][ny] != 0 and graph[nx][ny] < shark_size:
                fish.append((nx, ny, count + 1))
                flag = count

            visited[nx][ny] = True
            q.append((nx, ny, count + 1))

    if len(fish) > 0:

        fish.sort()

        x, y, t_move = fish[0][0], fish[0][1], fish[0][2]
        time += t_move

        eat += 1
        graph[x][y] = 0

        if eat == shark_size:

            shark_size += 1
            eat = 0

        start_x, start_y = x, y

    else:
        break

print(time)