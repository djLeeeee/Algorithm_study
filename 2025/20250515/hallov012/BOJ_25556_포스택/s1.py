import sys
sys.stdin = open('input.txt')

n = int(input())
a_lst = list(map(int, input().split()))
stacks = [[] for _ in range(4)]

ans = 'YES'
for a in a_lst:
    flag = False
    for i in range(4):
        if not stacks[i] or stacks[i][-1] < a:
            stacks[i].append(a)
            flag = True
            break
    if not flag:
        ans = 'NO'
        break
print(ans)


