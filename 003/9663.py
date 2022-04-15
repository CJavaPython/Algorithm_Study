import sys
input=sys.stdin.readline
N=int(input())

visited=[False] * (N*N)
#N*N 체스판 위에 퀸 N 개를 서로 공격할 수 없게 놓는 방법의 개수
def bf():
    return