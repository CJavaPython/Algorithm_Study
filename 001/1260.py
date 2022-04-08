#그래프를 dfs, bfs로 탐색한 결과
import sys
import deque from collections
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

def bfs():


graph = []
for i in range(M):
    graph.append(list(map(int,read().split())))
graph.sort()
#dfs metric: visited
visited = [False] * N
dfs(graph, V, visited)

