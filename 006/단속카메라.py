def solution(routes):
    answer = 0
    r = sorted(routes, reverse=True)
    if len(r)==1: return 1
    camera=30001
    for i in range(len(r)):
        if i==0:
            pass
        elif r[i][0]<=camera<=r[i][1]:
            continue
        if camera>r[i][0]:
            camera=r[i][0]
            answer+=1
    return answer