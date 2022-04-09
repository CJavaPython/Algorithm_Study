from collections import deque
import sys
read=sys.stdin.readline
N = int(read())
graph=[]
for _ in range(N):
    graph.append(list(map(int, read().split())))
#방향 : 오른쪽과 아래 == visited queue는 필요없다
dx = [1, 0]
dy = [0, 1]
#jump 방향이 오른쪽 + 아래 혼합은 불가능
def bfs(x, y):
    queue=deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        jump=graph[x][y]
        #움직이지 않는 경우의 수를 생각해야 했다. 85%에서 넘어가지 않던 이유
        if jump == 0:
            print("Hing")
            return
        for i in range(2):
            nx = x + dx[i] * jump
            ny = y + dy[i] * jump
            if nx > N-1 or ny > N-1 : 
                continue
            elif nx == N-1 and ny == N-1:
                print("HaruHaru")
                return
            else:
                queue.append((nx, ny))                        
    print("Hing")
    return
#start : (0,0)
bfs(0,0)