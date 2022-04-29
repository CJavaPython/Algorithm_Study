import sys

input = sys.stdin.readline



#n은 탐색범위 m은 고를 개수 ex: n - 5 , m - 3  123 , 124 , 125 이런식
n,m = map(int,input().split())

visited = [False for _ in range(n+1)]

tlist = [(i+1) for i in range(n)]

arr = []



#순열 1,2 와 2,1 순서 달라서 ㄱㅊ (중복허용) N개중에 중복을 허용해서 M개 고르는 경우 1,1 2,2는 안뎀
def permutation(depth):

    if depth == m:
        print(*arr)
        return

    for i in tlist:
        if i not in arr:
            arr.append(i)
            permutation(depth + 1)
            arr.pop()

def permutation2(depth):

    if depth == m:
        print(*arr)
        return

    for i in tlist:
        if not visited[i]:

            arr.append(i)
            visited[i] = True

            permutation(len(arr))

            arr.pop()
            visited[i] = False

comb_list = []

#조합 1,2 와 2,1은 순서가 달라도 구성 원소가 같아서 안됨. 즉 N개중 M개를 고르는데 중복 허용 X
def combination(depth):

    if depth == m:
        #print(arr)
        comb_list.append(arr[:])

        return

    for i in range(n):

        if not visited[i]:

            arr.append(i+1)
            visited[i] = True

            combination(depth+1)
            arr.pop()

            for j in range(i+1,n):
                visited[j] = False

combination(0)
print(comb_list)