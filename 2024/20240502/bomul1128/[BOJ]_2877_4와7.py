# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/2877
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=2877&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
n = int(input())
s = ""
while n > 0:
    if n % 2:
        s += "4"
    else:
        s += "7"
        n -= 1
    n //= 2
print(s[::-1])
