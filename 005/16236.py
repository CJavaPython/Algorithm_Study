from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count=[0]*(N+1)
space=[]
shark_size=2
time=0
start = []
for i in range(N):
    space.append(list(map(int, input().split())))
    for j in range(N):
        if space[i][j]!=0 and space[i][j]!=9:
            count[space[i][j]]+=1
        if space[i][j]==9:
            start.append(i)
            start.append(j)
print(count)
#전략 : x,y값을 넣는다
#처음에 count를 살펴본다 : 만약 count중에서 현재 샤크보다 작은 값 없으면 return 값으로 이를 알린다
#bfs를 돌려서, 가장 빨리 보이는 샤크보다 작은 값을 찾는다 <- 이 때마다 visited queue새로 생성 <- 처음 시작위치는 visited
#찾으면서 한 번 움직일 때마다 time도 +1 해준다
#아기 상어의 위치, 샤크의 크기 + 1, time을 return해준다.
#while문이 끝났는데도 못찾았으면 return 값으로 이를 알린다
#문제가 생겼을 경우의 return값 : 
#이를 반복한다.
def bfs(x, y, shark_size, time):
    q = deque()
    q.append((x,y,time))
    mama_shark=1
    for i in range(shark_size):
        if count[i]>0:
            mama_shark=0
            break
    if mama_shark==1:
        return x, y, -1, time
    X=x
    Y=y
    TIME=time
    visited=[[False] * N for _ in range(N)]
    visited[x][y]=True
    while q:
        x, y, time = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<N:
                if space[nx][ny]>=shark_size and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    q.append((nx,ny,time+1))
                elif space[nx][ny]==0 and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    q.append((nx,ny,time+1))
                elif space[nx][ny]>0 and visited[nx][ny]==False:
                    time+=1
                    shark_size+=1
                    space[nx][ny]=0
                    return nx, ny, shark_size, time
    return X, Y, -1, TIME
x=start[0]
y=start[1]
while True:
    x, y, shark_size, time = bfs(x, y, shark_size, time)
    print(time)
    if shark_size==-1:
        break
print(time)