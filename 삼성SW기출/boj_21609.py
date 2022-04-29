import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

answer = 0

black_block = -1
rainbow_block = 0
#0 보다 크고 m이하의 숫자면 일반블록이다

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def rotate_90():

    #반시계방향 90도회전 = 시계방향 90도 회전 3번

    rboard = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rboard[j][n-1-i] = board[i][j]

    return rboard

def rotate_180():

    rboard = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rboard[n-1-i][n-1-j] = board[i][j]

    return rboard

def rotate_270():
    #시계방향 270도 회전은 반시계방향 90도 회전과 같다
    rboard = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rboard[n-1-j][i] = board[i][j]

    return rboard    

# 0은 무지개 블럭 , -1은 검은 블럭이기때문에 -2 의값을 빈칸으로 설정
def remove():
    for x,y in block_list[-1][2]:
        board[x][y] = -2


def gravity():

    # 중력 적용을 위해 맨 위 부터가아닌 , 맨 아래에서 끌어 내리는 식으로 적용
    # for 문의 range(시작,끝,step)
    for i in range(n-2,-1,-1):
        for j in range(n):

                #만약 일반 블럭이라면 
                if board[i][j] >= 0:
                    temp = i
                    while True:
                        
                        # 끌어내릴 칸이 주어진 범위에 존재 하고 빈칸일 경우에
                        if 0 <= temp+1 < n and board[temp+1][j] == -2:
                            #현재 값을 끌어내림
                            board[temp+1][j] = board[temp][j]
                            #끌어내려진 칸은 빈칸이므로 -2로 초기화
                            board[temp][j] = -2
                            #계속 끌어내리기 위해 탐색할 행 +1
                            temp += 1

                        else:
                            break

# 가장 큰 블록 연결을 찾기위해 bfs로 탐색
def bfs(i,j,color):

    q = deque()
    q.append((i,j))

    visited[i][j] = True

    zero_block_cnt = 0

    blocks = [[i,j]] #탐색후 가장 큰 블럭을 삭제해야 하기 때문에 블럭을 구성하는 각 칸의 좌표가 필요함.
    z_blocks = [] #무지개블럭(0) 은 다른 색의 블럭과도 결합될 수 있기에 따로 관리

    while q: #bfs 시작

        x,y = q.popleft()

        for i in range(len(dx)):

            nx = x + dx[i]
            ny = y + dy[i]

            # 이동할 좌표가 범위안에 있거나 방문하지 않았고, 동일한 색의 블럭이거나 무지개 블럭이면 연결가능
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (board[nx][ny] == color or board[nx][ny] == 0):
                q.append((nx,ny))
                visited[nx][ny] = True
                blocks.append([nx,ny]) #연결한 블럭 좌표 저장

                if board[nx][ny] == 0: #우선순위에 무지개 블럭의 개수도 포함되어 있기에 한번더 체크
                    zero_block_cnt += 1
                    z_blocks.append([nx,ny])

    for x,y in z_blocks: # 무지개 블럭은 다른색의 블럭과도 결합될 수 있기 때문에 visited false로 다음탐색때도 탐색을 가능하게 함
        visited[x][y] = False    

    return [len(blocks),zero_block_cnt,blocks] # 우선순위 : 크기가 가장큰블럭 (len-block) , 크기가 같은 블럭일경우 무지개 블럭의 개수가 많은게 우선순위 더높고, 마지막으론 행과 열의 번호가 가장 작은 블럭


while True:

    visited = [[False] * n for _ in range(n)] # 매 반복 마다 초기화 시켜줘야함

    block_list = [] #후보 블럭 리스트를 저장하기 위함


    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and not visited[i][j]: #검은색블록은 포함하면안되서 0인 무지개블록과 0보다큰 일반블럭일 경우에만  + 방문하지않은 경우
                chunk_block = bfs(i,j,board[i][j]) #탐색좌표와 색깔을 넣어주고 탐색하여 블럭 덩어리를 리턴값으로 받음 block((블럭개수,0인블럭개수,각 블록의 좌표))

                if chunk_block[0] >= 2: # 연결된 블럭의 개수가 2개 이상이라면 후보 리스트에 append
                    block_list.append(chunk_block)


    block_list.sort() #크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.


    if len(block_list) < 1: #블록리스트 크기가 1보다 작다는건 모든 탐색을 마쳤다는 뜻
        break

    answer += block_list[-1][0] ** 2 #제거한 블록의 개수의 제곱 만큼이 점수

    remove() #해당 블록 제거
    gravity() #중력 적용
    board = rotate_270() #반시계방향 90도 회전

    '''
    #시계방향으로 90도 회전 3번이면 반시계 90도와 같음
    for i in range(3): 
        board = rotate_90()
    '''

    gravity() #중력 적용   


print(answer)