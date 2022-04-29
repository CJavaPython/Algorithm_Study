import sys
from collections import deque

input = sys.stdin.readline

# 0 북쪽 , 1 동쪽 , 2 남쪽 , 3 서쪽
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n , m = map(int,input().split())

start_r,start_c,start_d = map(int,input().split())


board = [list(map(int,input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

answer = 0

def turn_left(d):

    if d == 0: #북쪽에서 왼쪽으로  회전하면 서쪽
        return 3

    elif d == 1: #동쪽에서 왼쪽으로 회전하면 북쪽
        return 0

    elif d == 2: #남쪽에서 왼쪽으로 회전하면 동쪽
        return 1

    elif d == 3: #서쪽에서 왼쪽으로 회전하면 남쪽
        return 2

def go_back(d):

    if d == 0: #북쪽 바라보다 후진하면 남쪽
        return 2

    elif d == 1: #동쪽에서 후진하면 서쪽
        return 3

    elif d == 2: #남쪽에서 후진하면 북쪽
        return 0

    elif d == 3: #서쪽에서 후진하면 덩쩍
        return 1


def bfs(r,c,d):

    global answer

    q = deque()
    q.append((r,c,d))

    #board[r][c] = 2 #조건 1 현재 위치 청소 후 청소한 칸의 개수 증가 (answer + 1)
    visited[r][c] = True
    answer += 1

    while q:

        x,y,d = q.popleft() #bfs
        temp_d = d


        for i in range(len(dx)): #4번 탐색하기위해 이렇게함.

            temp_d = turn_left(temp_d) #조건 2.a 를위해 왼쪽으로 회전시킴

            nx = x + dx[temp_d] #왼쪽으로 한칸 전진
            ny = y + dy[temp_d]

            #if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0: #만약 한칸전진한 좌표가 주어진 board 안에 있고 청소를 하지 않은 공간이라면 (1=벽, 2=청소끝남[2대신 visited써도됨])
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and not visited[nx][ny]: 
            
                visited[nx][ny] = True #현재위치 청소후 청소한 칸의 개수 증가
                answer += 1 

                q.append((nx,ny,temp_d)) #다음 탐색을 위해 다음 좌표와 방향을 큐에 넣음
                break # 바로 다음 탐색을 진행해야하기에 break

            elif i == 3: # i의값은 4번탐색하기에 0,1,2,3 으로 증가됨 즉 i가 3일경우엔 2.b 조건실행
               
                nx = x + dx[go_back(d)]
                ny = y + dy[go_back(d)]
                q.append((nx,ny,d))

                if board[nx][ny] == 1: # 다탐색했는데 뒤가 벽이면 종료
                    print(answer)
                    return

bfs(start_r,start_c,start_d)
           