import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, s_atk = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * (n+1)
l, r = 0, n * 1000000 * 1000000
ans = 0
while l <= r:
    m = (l + r) // 2
    max_hp = m
    hp, atk = m, s_atk
    for t, a, h in rooms:
        if t == 1:
            cnt = h // atk
            if h % atk:
                cnt += 1
            hp -= a * (cnt-1)
        else:
            atk += a
            hp += h
            if hp > max_hp:
                hp = max_hp
        if hp <= 0:
            l = m + 1
            break
    else:
        r = m - 1
        ans = m
print(ans)
