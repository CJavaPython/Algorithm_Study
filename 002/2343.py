import sys
input=sys.stdin.readline
N,M=map(int,input().split())
#블루레이 최소크기 찾기
#N : 블루레이에 들어갈 수 있는 강의의 수
#M : 블루레이 수
#다음줄부터 강의의 길이가 순서대로 들어옴
lectures=[int(input) for _ in range(N)]
start, end = max(lectures), sum(lectures)
while start<=end:
    mid=start+end//2
    count=0
    play_time=0
    for l in lectures:
        #play_time이 M보다 커지면 새로운 dvd 필요
        if play_time + l > mid:
            count+=1
            play_time=0
        play_time+=1
    count+=1 if play_time else 0
    #블루레이 수보다 큰지 작은지 체크
    if count<=M:
        end=mid-1
    else:
        start=mid+1
print(start)