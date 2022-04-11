import sys
input=sys.stdin.readline
N=int(input())
start=0
end=N
while start<=end:
    mid=(start+end)//2
    if mid**2<N:
        start=mid+1
    else:
        end=mid-1
print(start)