import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def char_to_num(s):
    return ord(s) - m

def num_to_char(x):
    return chr(x+m)

def find(tmp, cnt):
    if cnt == len(S):
        print(tmp)
        return
    for i in range(k):
        if s_cnt[i]:
            s_cnt[i] -= 1
            find(tmp + num_to_char(i), cnt+1)
            s_cnt[i] += 1

n = int(input())
m = 97
k = 122-97+1
for _ in range(n):
    S = input().rstrip()
    s_cnt = [0] * k
    for s in S:
        s_cnt[char_to_num(s)] += 1
    ans = set()
    find('', 0)
