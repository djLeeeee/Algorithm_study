# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/2251
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=2251&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from collections import defaultdict

a, b, c = map(int, input().split())
state = [(0, 0, c)]
visited = defaultdict(bool)
visited[(0, 0, c)] = True
ans = [False] * (c + 1)
ans[c] = True
limit = (a, b, c)
while state:
    s = state.pop()
    for i in range(3):
        for j in range(3):
            if i != j and s[i] and (r := limit[j] - s[j]):
                rr = min(s[i], r)
                ns = list(s)
                ns[i] -= rr
                ns[j] += rr
                ns = tuple(ns)
                if not visited[ns]:
                    visited[ns] = True
                    state.append(ns)
                    if not ns[0]:
                        ans[ns[2]] = True
print(*[i for i in range(c + 1) if ans[i]])
