# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/2437
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=2437&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
def solve(arr):
    arr.sort()
    if arr[0] > 1:
        return 1
    ans = 1
    for a in arr[1:]:
        if a > ans + 1:
            return ans + 1
        ans += a
    return ans + 1


n = int(input())
arr = list(map(int, input().split()))
print(solve(arr))
