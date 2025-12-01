import sys
sys.stdin = open('input.txt')

n = int(input())
str = input().strip()
stack = []
ans = [(-1, -2)]
for (i, s) in enumerate(str):
    if s == '(':
        stack.append(i)
    elif stack:
        tmp = stack.pop()
        while ans and ans[-1][0] > tmp:
            ans.pop()
        # 연속되는 인덱스면 해당 부분의 시작점으로 갱신
        if ans and ans[-1][1] + 1 == tmp:
            tmp = ans.pop()[0]
        ans.append((tmp, i))

ans.sort(key=lambda x: x[0] - x[1])
x, y = ans[0]
print(y - x + 1)