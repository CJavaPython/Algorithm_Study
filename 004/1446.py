import sys
input = sys.stdin.readline
N, D = map(int,input().split())
#계수정렬 사용 - D+1로 해야 D만큼 들어감
#최단거리는 목적지에 업데이트하면 된다(목적지까지 가기 위한 최단거리)
route=[i for i in range(D+1)]
path=[]

for _ in range(N):
    #0 : source 1 : dest 2 : path_len
    path.append(list(map(int,input().split())))
short_path= sorted(path)

for i in range(len(short_path)):
    #"소스까지의 거리 + 지름길 길이"(이전 노드 + 지름길) 값이 "현재 목적지까지의 거리" (지금 노드) 보다 작다면, 업데이트 해줌.
    #최단거리 목적지에 업데이트되면, 그 이후의 거리들도 모두 업데이트.
    #루트 너머로 가는 지름길도 있음
    if short_path[i][0] <= D and short_path[i][1] <= D:
        if route[short_path[i][1]] >= route[short_path[i][0]] + short_path[i][2]:
            route[short_path[i][1]] = route[short_path[i][0]] + short_path[i][2]
            for j in range(short_path[i][1]+1, len(route)):
                route[j] = min(route[j], route[j-1] + 1)

print(route[D])