from collections import deque
import sys
input = sys.stdin.readline
#500*500 board
board = [[0 for i in range(501)] for j in range(501)]
visited = [[False] * 501 for j in range(501)]
N = int(input())
for i in range(N):
    x1, y1, x2, y2 = map(int,input().split())
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            board[x][y]=1

M = int(input())
for j in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            board[x][y]=1000

board[0][0]=0
visited[0][0]=True
hp = 1000
#방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
q.append((0,0))
#route true false
tf = False

while q:
    x,y = q.popleft()
    if x == 500 and y == 500:
        tf = True
        break 
    elif hp < 0:
        break       
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx <= 500 and ny >= 0 and ny <= 500 and visited[nx][ny]==False:
            if board[nx][ny] == 0:
                visited[nx][ny]=True
                q.appendleft((nx, ny))
            elif board[nx][ny] == 1:
                hp-=1
                visited[nx][ny]=True
                q.appendleft((nx, ny))

#갈 수 없으면 -1
#갈 수 있으면 위험지역에서 빠진 hp
if tf:
    print(hp)
else:
    print(-1)