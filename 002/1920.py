import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int, input().split()))
A.sort()
M=int(input())
M_list=list(map(int, input().split()))
for x in M_list:
    start, end = 0, len(A)-1
    tf=0
    while start<=end:
        mid=(start+end)//2
        if x>A[mid]:
            start=mid+1
        elif x<A[mid]:
            end=mid-1
        else:
            tf=1
            break
    print(tf)