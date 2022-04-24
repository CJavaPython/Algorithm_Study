import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
graph = [[0]*n for _ in range(n)]

fav_list = defaultdict(list)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

answer = 0

for _ in range(n**2):

    student,a,b,c,d = map(int,input().split())
    fav_list[student] = [a,b,c,d]

def z_count(x,y):

    z = 0

    for i in range(len(dx)):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                z += 1

    return z

def like_count(x,y,likes):

    l = 0

    for i in range(len(dx)):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] in likes:
                l += 1

    return l

for student,likes in fav_list.items():

    candi = list()

    for i in range(n):
        for j in range(n):

            like = 0
            empty = 0

            if graph[i][j] == 0:
                like = like_count(i,j,likes)
                empty = z_count(i,j)

            candi.append([like,empty,i,j])

    candi.sort()
    graph[candi[-1][2]][candi[-1][3]] = student        
    

for i in range(n):
    for j in range(n):
        cnt = like_count(i,j,fav_list[graph[i][j]])

        if cnt == 0:
            answer += 0

        elif cnt == 1:
            answer += 1

        elif cnt == 2:
            answer += 10

        elif cnt == 3:
            answer += 100

        elif cnt == 4:
            answer += 1000

print(answer) 



        


    