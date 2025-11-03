import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(now, now_c):
    global ans
    state, money, g_lst = rooms[now]
    if state == 'L':
        if now_c < money:
            now_c = money
    elif state == 'T':
        now_c -= money
        if now_c < 0:
            return
    if now == n:
        ans = True
        return
    for next in g_lst:
        if not visited[next]:
            visited[next] = 1
            find(next, now_c)
            visited[next] = 0

while True:
    n = int(input())
    if not n:
        break
    rooms = [[]]
    for _ in range(n):
        [state, money, *g_lst] = list(input().split())
        rooms.append((state, int(money), list(map(int, g_lst[:-1]))))

    visited = [0] * (n+1)
    visited[1] = 1
    ans = False
    find(1, 0)
    print('Yes' if ans else 'No')
