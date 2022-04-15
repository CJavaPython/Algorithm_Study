import sys
input=sys.stdin.readline
N=int(input())
#N의 정수 제곱근 구하기
#0=0, 1=1, 2와 3은 없다
#4부터는 그 수 / 2 에 대해서만 찾아보면 됨
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    start, end = 2, int(N/2)
    while start<=end:
        mid=(start+end)//2
        target=mid*mid
        if target>N:
            end=mid-1
        elif target>N:
            start=mid+1
        else:
            break
    print(int(start))