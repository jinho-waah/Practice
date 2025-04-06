from collections import deque

def solution(cacheSize, cities):
    time = 0
    cache = deque()

    for city in cities:
        city = city.lower()

        if city in cache:
            # cache hit
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            # cache miss
            if cacheSize > 0:
                if len(cache) >= cacheSize:
                    cache.popleft()
                cache.append(city)
            time += 5

    return time