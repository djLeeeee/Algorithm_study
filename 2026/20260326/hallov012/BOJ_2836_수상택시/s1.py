import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    if s > e:
        arr.append((e, s))

if not arr:
    print(m)
    exit()

arr.sort(key= lambda x: (x[0], -x[1]))
tmp = 0
t_s, t_e = arr[0]
for i in range(1, len(arr)):
    s, e = arr[i]
    if s > t_e:
        tmp += t_e - t_s
        t_s, t_e = s, e
    else:
        if t_e < e:
            t_e = e
tmp += t_e - t_s
print(m + tmp * 2)