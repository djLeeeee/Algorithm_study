import sys
sys.stdin = open('input.txt')

n = int(input())
m = int(input())
s = input().rstrip()
ans = 0
idx = 0
piece = 0
# IOI의 갯수를 센다
while idx < m-2:
    if s[idx] == 'I' and s[idx+1] == 'O' and s[idx+2] == 'I':
        piece += 1
        idx += 2
    else:
        if piece - n >= 0:
            ans += piece - n + 1
        piece = 0
        idx += 1
if piece - n >= 0:
    ans += piece - n + 1

print(ans)