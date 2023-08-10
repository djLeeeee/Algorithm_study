import re, sys

input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    string = input().strip()
    regex = re.compile('(100+1+|01)+')
    if regex.fullmatch(string):
        print('YES')
    else:
        print('NO')
