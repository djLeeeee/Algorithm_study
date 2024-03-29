# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/16934
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=16934&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from sys import stdin

input = stdin.readline

trie = {}
for _ in range(int(input())):
    s = input().strip()
    cur = trie
    ans = ""
    flag = False
    for c in s:
        if not flag:
            ans += c
        if c not in cur:
            cur[c] = {}
        cur = cur[c]
        if not cur and not flag:
            flag = True
    cur["*"] = cur.get("*", 0) + 1
    if not flag and cur["*"] > 1:
        ans += str(cur["*"])
    print(ans)
