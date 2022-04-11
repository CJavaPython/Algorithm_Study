import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int, input().split()))
A.sort()
M=int(input())
M_list=list(map(int, input().split()))
for x in M_list:
    start, end = min(A), max(A)
    tf=0
    while start<=end:
        mid=(start+end)//2
        if x>mid:
            start+=1
        elif x<mid:
            end-=1
        else:
            tf=1
            break
    print(tf)