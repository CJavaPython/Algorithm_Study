import sys
input=sys.stdin.readline
N=int(input())
#N의 정수 제곱근 구하기
#0=0, 1=1, 2와 3은 없다
#4부터는 그 수 / 2 에 대해서만 찾아보면 됨
def binary():
    
start, end = 