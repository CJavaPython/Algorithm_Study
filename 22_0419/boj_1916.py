import sys
import heapq


input = sys.stdin.readline


n = int(input())
m = int(input())

INF = int(1e9)

edges = [[] for _ in range(n+1)]

distance = [INF] * (n+1)
distance2 = [987654321] * (n+1)

for _ in range(m):
    start,end,cost = map(int,input().split())
    edges[start].append((end,cost))


start_node, end_node = map(int,input().split())

def dijkstra(start):

    q = []

    heapq.heappush(q,(0,start))

    distance[start] = 0 

    while q:

        dist,now_node = heapq.heappop(q)

        if distance[now_node] < dist:
            continue

        for i in edges[now_node]:

            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


dijkstra(start_node)

print(distance[end_node])

