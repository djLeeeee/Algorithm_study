# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/1700
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=1700&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if n >= k:
        return 0
    holes = set()
    cnt = 0
    for i, v in enumerate(arr):
        if v in holes:
            continue
        if len(holes) < n:
            holes.add(v)
        else:
            remain = arr[i + 1:] + list(holes)
            m = max(holes, key=lambda x: remain.index(x))
            holes.remove(m)
            holes.add(v)
            cnt += 1
    return cnt


if __name__ == '__main__':
    print(solve())
