def solution(cacheSize, cities):
    if not cacheSize:
        return len(cities) * 5
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            answer += 5
    return answer

input_lst = [
    [3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]],
    [3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]],
    [2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]],
    [5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]],
    [2, ["Jeju", "Pangyo", "NewYork", "newyork"]],
    [0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]]
]

for a, b in input_lst:
    print(solution(a, b))