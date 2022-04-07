import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

visited_bfs = [False] * (N + 1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def bfs(start_v):

    q = deque([start_v])
    visited_bfs[start_v] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True

bfs(1)
print(visited_bfs.count(True)-1)
