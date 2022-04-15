import sys
input=sys.stdin.readline
N=int(input())

visited=[[False]*(N) for _ in range(N)]
#N*N 체스판 위에 퀸 N 개를 서로 공격할 수 없게 놓는 방법의 개수
def backtracking(x, y):
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                k=0
                while i-k>=0 and j-k>=0:
                    visited[i-k][j-k]=True
                    k+=1
                k=0
                while i+k<N and j+k<N:
                    visited[i+k][j+k]=True
                    k+=1
                k=0
                while i-k>=0:
                    visited[i-k]=True
                    k+=1
                k=0
                while i+k<N:
                    visited[i+k]=True
                    k+=1
                k=0
                while j-k>=0:
                    visited[j-k]=True
                    k+=1
                k=0
                while j+k>=0:
                    visited[j+k]=True
                    k+=1
                
            
backtracking(0,0)