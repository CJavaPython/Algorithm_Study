#그래프를 dfs, bfs로 탐색한 결과
import sys
from collections import deque
read = sys.stdin.readline
N, M, V = map(int, read().split())
#dfs : 재귀
#bfs : deque
def dfs(graph, v, visited):
    visited[v-1] = True
    print(v, end=' ')
    for x in graph:
        if v in x:
            idx = (x.index(v)+1)%2
            if visited[x[idx]-1] == False:
                dfs(graph,x[idx],visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v-1]=True
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for y in graph:
            if v in y:
                idx=(y.index(v)+1)%2
                if visited[y[idx]-1]==False:
                    queue.append(y[idx])
                    visited[y[idx]-1]=True


graph = []
for i in range(M):
    graph.append(list(map(int,read().split())))
dfs_graph=graph.sort()
bfs_graph=graph.sort()
dfs_visited=[False] * N
bfs_visited=[False] * N

dfs(graph, V, dfs_visited)
print()
bfs(graph, V, bfs_visited)