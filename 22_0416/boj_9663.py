import sys

input = sys.stdin.readline

n = int(input())

answer = 0

a = [False]*n #수직
b = [False]*(2*n-1) #오른쪽 대각선
c = [False]*(2*n-1) #왼쪽 대각선

def back(i):

    global answer

    if i == n: #퀸을 n개 만큼 놓았으면 경우의수 + 1
        answer += 1
        return

    for j in range(n): # 모든 열 순회

        if (not a[j] and not b[i+j] and not c[i-j+n-1]): # 수직 , 좌/우 대각선이 모두 false 일때
            a[j] = b[i+j] = c[i-j+n-1] = True # 시도
            back(i+1) #다음줄 진행
            a[j] = b[i+j] = c[i-j+n-1] = False # 안되면 백트래킹

back(0)
print(answer)