def solution(routes):
    answer = 0
    r = sorted(routes)
    if len(r)==1: return 1
    start=30001
    end=-30001
    for i in range(len(r)):
        if i==0:
            pass
        elif start<=r[i][0]<=end or start<=r[i][1]<=end:
            continue
        answer+=1
        if start>r[i][0]:
            start=r[i][0]
        if end<r[i][1]:
            end=r[i][1]
    return answer
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))