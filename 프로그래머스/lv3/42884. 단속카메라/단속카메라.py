def solution(routes):
    routes.sort()
    L = len(routes)
    marker = [[] for _ in range(60001)]
    cars = [0] * (L + 1)
    onroad = []

    camera = 0
    for idx in range(L):
        dep, _ = routes[idx]
        marker[dep+30000].append(idx+1)
    
    for idx in range(L):
        _, des = routes[idx]
        marker[des+30000].append(idx+1)
    
    for idx in range(60001):
        if marker[idx]:
            flag = 0
            for car in marker[idx]:
                if cars[car] == 0:
                    cars[car] = 1
                    onroad.append(car)
                elif cars[car] == 1:
                    flag = 1
            if flag:
                camera += 1
                while onroad:
                    shot = onroad.pop()
                    cars[shot] = 2
    return camera