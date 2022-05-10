import sys
#N개의 박스, M개의 색상
#조커는 색이 다른 카드를 보관해도 된다
#첫째 줄 박스의 개수 N, 카드 색상 종류 M
#둘째 줄부터 박스에 들어있는 카드 수 입력
#박스 주어지면, 문제 조건 만족하게 하는 최소 이동?
input = sys.stdin.readline
N, M = map(int,input().split())

min_row=[51 for _ in range(N)]
card = [list(map(int,input().split())) for i in range(N)]
for i in range(N):
    for j in range(M):
        if card[i][j] != 0 and min_row[i]==51:
            min_row[i]=0
        if card[i][j] != 0:
            min_row[i]=min_row[i]+1


count=[]
for joker in range(N):
    tmp_count=0

    visited=[False for _ in range(M)]
    k = min_row.index(min(min_row))
    if k == 51:
        break
    for i in range(k, k+N):
        i = i % N
        if joker==i:
            continue
        for j in range(M):
            if card[i][j]!=0 and not visited[j]:
                visited[j]=True
            elif card[i][j]!=0 and visited[j]:
                tmp_count+=1
                break
    count.append(tmp_count)
print(min(count))
print(count)