#그래프를 dfs, bfs로 탐색한 결과
import sys
from collections import deque
read = sys.stdin.readline
N, M, V = map(int, read().split())
#dfs : 재귀
#bfs : deque
#숫자 헷갈리지 않게 하려고 N+1
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b=map(int, read().split())
    #양방향
    graph[a].append(b)
    graph[b].append(a)
#dfs : 재귀함수
def dfs(graph, v, visited):
    print(v,end=' ')
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
#bfs : deque
def bfs(graph, v, visited):
    visited[v]=True
    queue=deque([v]) 
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
#작은 순서대로
for i in range(1, N+1):
    graph[i].sort()
visited = [False] * (N+1)
dfs(graph, V, visited)
print()
visited = [False] * (N+1)
bfs(graph, V, visited)