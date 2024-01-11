# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/2212
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=2212&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()
dist = []
for i in range(1, n):
    dist.append(arr[i] - arr[i - 1])
dist.sort()
print(sum(dist[:n - m]) if n > m else 0)
