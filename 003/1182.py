import sys 
input=sys.stdin.readline
n,s=map(int,input().split())

elements=list(map(int, input().split()))

visited=[False]*n
count=0

def backtracking(depth, subset):
    global count
    if depth==n-1:
        return
    if subset==s:
        count+=1
        return
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            backtracking(i, subset+elements[i])
            subset-=elements[i]
            visited[i]=False
backtracking(0, 0)
print(count)