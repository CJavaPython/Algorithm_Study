import sys

input = sys.stdin.readline

n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

# 0은 빈칸 1은 집 2는 치킨집이다.

home  = list()
chick_shop = list()
chick_comblist = list()

answer = int(1e9)


# 맵을 순회하며 집과 치킨집의 좌표를 저장
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append([i,j])
        elif board[i][j] == 2:
            chick_shop.append([i,j])


temp = [] #조합의 임시리스트
visited = [False] * (len(chick_shop) + 1) #조합에서 중복방지를 위한 visited


# 주어진 모든 치킨집 에대한 조합 좌표 반환
def chick_combination(depth):

    if depth == m:
        chick_comblist.append(temp[:])
        return

    for i in range(len(chick_shop)):
        
        if not visited[i]:

            temp.append(chick_shop[i])
            visited[i] = True

            chick_combination(depth+1)

            temp.pop()
            
            for j in range(i+1,len(chick_shop)):
                visited[j] = False

#해밀턴 거리 구하는 식 |r1-r2| + |c1-c2|
def min_distance(home_cord,shop_cord):

    return abs(home_cord[0] - shop_cord[0]) + abs(home_cord[1] - shop_cord[1])


#depth 0부터 주어진 치킨집들의 좌표에 대한 모든 조합을 만들어 chick_comblist에 저장
chick_combination(0)


#조합으로 고른 각각의 치킨집에 대하여
for i in chick_comblist:

    temp_min = 0

    # 치킨집 1에 대해서 모든 집에 대한 치킨 거리를 구해서 그 최소값을 저장
    for j in home:
        minval = int(1e9)

        for k in i:
            dist = min_distance(j,k)
            minval = min(minval,dist)

        #한 치킨집에 대한 최소값을 저장
        temp_min += minval

    answer = min(answer,temp_min)

print(answer)