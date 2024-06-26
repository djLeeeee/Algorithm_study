# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/14226
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=14226&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
def update(sticker, clip, time):
    if (sticker, clip) in checker:
        if checker[(sticker, clip)] > time:
            checker[(sticker, clip)] = time
            return True
        return False
    checker[(sticker, clip)] = time
    return True


n = int(input())
checker = {}
checker[(1, 0)] = 0
states = [(1, 0, 0)]
ans = 0
for s, c, t in states:
    if s == n:
        ans = t
        break
    if c > 0 and s < n:
        if update(s + c, c, t + 1):
            states.append((s + c, c, t + 1))
    if update(s, s, t + 1):
        states.append((s, s, t + 1))
    if update(s - 1, c, t + 1):
        states.append((s - 1, c, t + 1))
print(ans)
