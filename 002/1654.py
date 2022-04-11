import sys
input=sys.stdin.readline
K,N=map(int,input().split())
#랜선 최소길이
#K : 랜선 개수
#N : 같은 길이의 랜선으로 자른 것 개수 / 정수 단위로 잘라야함
#자르고 남은거 버림
lan=[int(input()) for _ in range(K)]
start, end = 1, max(lan)
mid = 0
while start<=end:
    mid = (start+end) // 2
    lines = 0
    for i in lan:
        lines += i // mid#분할된 랜선 수
    if lines>=N:
        start=mid+1
    else:
        end=mid-1
print(end)