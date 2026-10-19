# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/17680
# Submission: 2026-07-02 14:18:12 Python3 정답 100 /
def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.pop(cache.index(city))
        else:
            answer += 5
        cache.append(city)
        if len(cache) > cacheSize:
            cache.pop(0)
    return answer
