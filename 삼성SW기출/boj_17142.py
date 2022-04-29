import sys
from collections import deque
from copy import deepcopy


input = sys.stdin.readline

# 0은 빈 칸, 1은 벽, 2는 바이러스

n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

virus_list = list()
virus_comb_list = list()

blank_cnt = 0

answer = int(1e9)


# 각각의 바이러스의 좌표를 기록해놔야한다. 모든 바이러스의 위치로 탐색하지 않고, m개만 뽑아서 (조합) bfs든 dfs든 탐색을 진행하기 때문이다.
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus_list.append((i,j))
        if board[i][j] == 0:
            blank_cnt += 1


virus_visited_list = [False] * len(virus_list)


#      ↑ ← ↓ →  상 좌 하 우 방향으로 탐색 하게 만듬
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# maps 안에 0이 있는지 여부. 
# bfs로 모든 바이러스 전파가 끝났는데 0이 남아 있다면 더 이상 바이러스를 퍼뜨릴 수 없다는 의미.
def check(visited):
    for i in range(len(visited)):
        for j in range(len(visited)):
            if visited[i][j] == 0:
                return -1
    return 0


def bfs(virus_c_list):
    
    visited_map = [[False] * n for _ in range(n)]

    new_board = deepcopy(board) #조합상 가능한 모든 경우에수에대해 탐색해야하기에 deepcopy로 원본 배열 보존

    virus_cnt = 0

    q = deque()

    for i in virus_c_list:
        q.append((i[0],i[1],0))

    while q:

        x,y,cnt = q.popleft()

        visited_map[x][y] = True

        for i in range(len(dx)):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and new_board[nx][ny] != 1 and not visited_map[nx][ny] :
                
                visited_map[nx][ny] = True

                if new_board[nx][ny] == 0:
                    new_board[nx][ny] = 2
                    virus_cnt = cnt +1
                                   
                q.append((nx,ny,cnt+1))
                

    val = check(new_board)

    if val == 0:
        return virus_cnt
    
    else:
        return -1

temp = [] # 조합을 위한 임시 저장 리스트

def combination(depth):

    if depth == m:
        virus_comb_list.append(temp[:])
        return

    for i in range(len(virus_list)):

        if not virus_visited_list[i]:

            temp.append(virus_list[i])
            virus_visited_list[i] = True

            combination(depth+1)
            temp.pop()

            for j in range(i+1,len(virus_list)):
                virus_visited_list[j] = False


combination(0)
#print(virus_comb_list) #비활성 바이러스 위치들의 조합 ex 5c3 이면 5개중에서 3개골라서 가능한 경우 중복제거하고 전부

for i in virus_comb_list:

    res = bfs(i)

    if res != -1:

        answer = min(answer,res)


if answer == int(1e9):
    print(-1)
else:
    print(answer)


