import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(input())
a_lst = list(map(int, input().split()))
m = int(input())
b_lst = list(map(int, input().split()))

a_lst = deque(sorted(enumerate(a_lst), key=lambda x:(-x[1], x[0])))
b_lst = deque(sorted(enumerate(b_lst), key=lambda x:(-x[1], x[0])))

a_last, b_last = -1, -1
ans = []

while a_lst and b_lst:
    a_idx, a = a_lst[0]
    b_idx, b = b_lst[0]
    if a == b:
        flag = True
        if a_idx < a_last:
            a_lst.popleft()
            flag = False
        if b_idx < b_last:
            b_lst.popleft()
            flag = False
        if flag:
            ans.append(a)
            a_last, b_last = a_idx, b_idx
            a_lst.popleft()
            b_lst.popleft()
    elif a > b:
        a_lst.popleft()
    else:
        b_lst.popleft()

print(len(ans))
print(*ans)
