def solution(cacheSize, cities):
    cache = {}
    cached = set()
    call = 0
    answer = 0
    if cacheSize == 0: return 5 * len(cities)
    
    for city in cities:
        city = city.lower()
        if city in cached:
            cached.add(city)
            cache[city] = call
            answer += 1
        else:
            if cacheSize <= len(cached):
                old = sorted(cache.keys(), key=lambda x: cache[x])[0]
                cached.remove(old)
                del cache[old]
            cached.add(city)
            cache[city] = call
            answer += 5
        call += 1
    
    return answer