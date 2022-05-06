def solution(routes):
    
    answer = 0
    
    routes.sort(key = lambda x: x[1])
    cam = routes[0][1]
    
    for i in routes:
        if cam < i[0]:
            cam = i[1]
            answer += 1
    
    
    return answer + 1