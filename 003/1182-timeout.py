import sys 
input=sys.stdin.readline
n,s=map(int,input().split())

elements=list(map(int, input().split()))

visited=[False]*n
count=0

def backtracking(depth, subset):
    global count
    #n-1까지하면 마지막까지 탐방 x
    if depth==n:
        return
    subset+=elements[depth]
    if subset==s:
        count+=1
    for i in range(depth, n):
        if not visited[i]:
            visited[i]=True
            backtracking(depth+1,subset)
            subset-=elements[i]
            visited[i]=False
backtracking(0, 0)
print(count)