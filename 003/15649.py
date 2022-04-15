import sys
input=sys.stdin.readline
N,M=map(int,input().split())

result=[]
visited=[False]*(N+1)
def backtracking(depth):
    if depth==M:
        print(" ".join(map(str, result)))
        return
    for i in range(1,len(visited)):
        #처음 들어갈 때는 1
        #두 번째 들어갈 때는 1은 이미 visited 돼있으니 그것 이외의 값을 2차원에 배치
        if not visited[i]:
            visited[i]=True
            result.append(i)
            backtracking(depth+1)#1을 제외한 모든 숫자들의 visited가 이루어짐
            #for문이기 떄문에 False로 다시 바꿔줘도 문제 없을 것
            visited[i]=False
            result.pop()
    
#만약 순서대로 backtracking하지 않는다면?    
backtracking(0)