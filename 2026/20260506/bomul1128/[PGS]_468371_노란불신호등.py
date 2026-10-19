# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/468371
# Submission: 2026-05-14 15:44:30 / Python3 / 정답 100
def solution(signals):
    L = 3 * 10 ** 6
    
    def build(s):
        g, y, r = s
        part = [0] * g + [1] * y + [2] * r
        return part * (L // len(part) + 1)
        
    lights = [build(signal) for signal in signals]
    for i in range(L):
        if all(light[i] == 1 for light in lights):
            return i + 1
    return -1
