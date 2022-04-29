import sys

input = sys.stdin.readline

n = int(input())

A = list(map(int,input().split()))
b,c = map(int,input().split())

answer = 0

for i in range(len(A)):
    A[i] -= b
    answer += 1

    if A[i] > 0:
        answer += A[i] // c

        if A[i] % c != 0:
            answer +=1

print(answer)



