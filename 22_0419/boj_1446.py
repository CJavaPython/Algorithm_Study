import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


n,d = map(int,input().split())

road = [[] for _ in range(d+1)]

for i in range(d):
    road[i].append((i+1,1))

distance = [INF] * (d+1)

for _ in range(n):
    start,end,cost = map(int,input().split())

    if end > d:
        continue

    road[start].append((end,cost))

start_node = 0
end_node = d

def dijkstra(start):

    q = []

    heapq.heappush(q,(0,start))

    distance[start] = 0

    while q:
        
        dist,now_node = heapq.heappop(q)

        if distance[now_node] < dist:
            continue

        for i in road[now_node]:

            cost = dist + i[1] 

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start_node)
print(distance[d])


