import sys
import heapq



input = sys.stdin.readline


n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
edge = list()

parent = [i for i in range(n+1)]

answer = 0

for i in range(n):
    for j in range(i + 1, n):
        edge.append((graph[i][j], i, j))

edge.sort()


def find(x):
    
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union(a,b):

    rootA = find(a)
    rootB = find(b)

    if rootA > rootB:
        parent[rootA] = rootB

    else:
        parent[rootB] = rootA


for i in edge:

    cost,a,b = i

    if find(a) != find(b):
        union(a,b)
        answer += cost

print(answer) 
