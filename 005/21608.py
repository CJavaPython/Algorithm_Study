#구현 문제
#classroom : N*N grid
#stduents : n^2
#students num : 1~N*N
#배치 우선순위 1 : 좋아하는 학생이 가장 많이 인접
#배치 우선순위 2 : 인접한 칸 중 빈 칸이 가장 많은 칸
#배치 우선순위 3 : 행의 번호 가장 작은 순. 그것도 여러 개면 열 번호까지 고려.
#만족도 계산 : 인접한 칸에 앉은 좋아하는 학생 수 기준 - 0이면 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000 - 들의 합
import sys
from collections import deque
input = sys.stdin.readline
N=int(input())
student_list=[]
like_list=[]
score=[0,1,10,100,1000]
result=0
for _ in range(N*N):
    x=list(map(int, input().split()))
    student_list.append(x[0])
    like_list.append(x[1:])
visited=[[-1] * N for _ in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for s in range(len(student_list)):
    #count가 하나도 안 들어갈 경우 생각
    joint = 0
    loc = list()

    for i in range(N):
        for j in range(N):
            if visited[i][j] != -1:
                continue
            prior_count=0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx >= 0 and nx < N and ny >= 0 and ny < N:
                    if visited[nx][ny] in like_list[s]:
                        prior_count+=1
            #prior1
            if prior_count > joint:
                joint=prior_count
                loc=list()
                loc.append([i,j])
            elif prior_count == joint:
                loc.append([i,j])

    if len(loc)>1 or len(loc)==0:
        empty = 0
        empty_loc=list()
        for i, j in loc:
            empty_count=0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx >= 0 and nx < N and ny >= 0 and ny < N:
                    if visited[nx][ny]==-1:
                        empty_count+=1
            #prior2
            if empty_count > empty:
                empty=empty_count
                empty_loc=list()
                empty_loc.append([i,j])
            elif empty_count==empty:
                empty_loc.append([i,j])
        if len(empty_loc)>0:
            loc=list()
            loc.append(empty_loc[0])
        else:
            for i in range(N):
                for j in range(N):
                    if visited[i][j]!=-1:
                        loc.append([i,j])
                        break
                if len(loc)!=0:
                    break

    visited[loc[0][0]][loc[0][1]]=student_list[s]



for i in range(N):
    for j in range(N):
        v = student_list.index(visited[i][j])
        count=0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if visited[nx][ny] in like_list[v]:
                    count+=1
        result+=score[count]
print(result)