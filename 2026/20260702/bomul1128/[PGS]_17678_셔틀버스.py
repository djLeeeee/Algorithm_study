# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/17678
# Submission: 2026-07-02 15:40:16 Python3 정답 100 /
def solution(n, t, m, timetable):
    def transfer(char):
        h, m = map(int, char.split(':'))
        return h * 60 + m
    
    def rollback(num):
        h, m = divmod(num, 60)
        return f"{h:02d}:{m:02d}"
    
    arr = list(map(transfer, timetable))
    arr.sort(reverse=True)
    now = 540 - t
    ans = now
    for _ in range(n):
        now += t
        for _ in range(m):
            if arr and arr[-1] <= now:
                ans = arr.pop() - 1
            else:
                ans = now
                break
    return rollback(ans)
