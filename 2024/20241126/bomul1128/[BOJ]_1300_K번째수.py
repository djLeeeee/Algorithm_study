# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/1300
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=1300&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
n = int(input())
k = int(input())
left = 1
right = k
ans = 0
while left <= right:
    mid = (left + right) // 2
    tmp = 0
    for i in range(1, n + 1):
        tmp += min(mid // i, n)
    if tmp < k:
        left = mid + 1
    else:
        ans = mid
        right = mid - 1
print(ans)
