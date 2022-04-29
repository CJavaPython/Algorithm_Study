import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
graph = [[0]*n for _ in range(n)]

fav_list = defaultdict(list)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

answer = 0

for _ in range(n**2):

    student_list = list(map(int,input().split()))
    fav_list[student_list[0]] = student_list[1:]
    
def z_count(x,y): # 해당좌표와 인접한 칸의 0 의개수를 리턴

    z = 0

    for i in range(len(dx)):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                z += 1

    return z

def like_count(x,y,likes): # 해당좌표와 인접한 칸의 친한친구 명수를 리턴

    l = 0

    for i in range(len(dx)):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] in likes:
                l += 1

    return l

for student,likes in fav_list.items(): # 사전자료형 순회 학생번호 - 학생과친한친구리스트 모두 순회

    candi = list()

    for i in range(n):
        for j in range(n):

            like = 0
            empty = 0

            if graph[i][j] == 0: # 자리가 비어있으면
                like = like_count(i,j,likes) # 친한친구의 수
                empty = z_count(i,j) # 빈 자리의 수
                
                candi.append([like,empty,i,j]) #바로 결정하는것이 아닌 최적의 자리를 찾아야 하기에 후보 리스트를 만들어서 모든 경우의수를 체크함

    candi.sort(key = lambda x : (-x[0],-x[1],x[2],x[3])) # 문제에 제시된 우선순위대로 정렬
    graph[candi[0][2]][candi[0][3]] = student # sort결과 맨 앞에있는값이 우선순위가 제일 높기에 해당 좌표에 학생 배치   


# 학생들 전부 배치 후 만족도 조사를 위해 맵을 순회함
for i in range(n):
    for j in range(n):
        
        cnt = 0

        cnt = like_count(i,j,fav_list[graph[i][j]]) # 해당 학생 주변의 친한친구수를 세서

        # 만족도 점수를 부여함
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