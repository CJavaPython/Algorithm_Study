import sys
input = sys.stdin.readline
N=int(input())
M=int(input())
path=[]
edge=[]
for _ in range(M):
    path.append(list(map(int, input().split())))
    if path[0] not in edge:
        edge.append([path[0],100000])
    if path[1] not in edge:
        edge.append([path[1],100000])

s, d = map(int, input().split())

p = sorted(path)
e = sorted(edge)

result = 0
