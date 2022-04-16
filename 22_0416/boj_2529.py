import sys

input = sys.stdin.readline

k = int(input())
k_list = list(input().split())

answer = list()

visited = [False] * 10


def check(i,j,sign):
    if sign == '>':
        return i>j
    else:
        return i<j



def dfs(depth,num_string):

    global answer

    if depth == k+1:
        answer.append(num_string)
        return 


    for i in range(10):

        if not visited[i]:
            if depth == 0 or check(num_string[-1],str(i),k_list[depth-1]):
                
                visited[i] = True
                dfs(depth + 1, num_string+str(i))
                visited[i] = False



dfs(0,"")

print(max(answer))
print(min(answer))



