import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def sol(num, first, second, f_dist, s_dist):
    global ans
    f_cnt = min(num, cnt[first])
    s_cnt = num - f_cnt
    ans += (f_cnt * f_dist) + (s_cnt * s_dist)
    cnt[first] -= f_cnt
    cnt[second] -= s_cnt

while True:
    n, a, b = map(int, input().split())
    if (n, a, b) == (0, 0, 0):
        break
    teams = [list(map(int, input().split())) for _ in range(n)]
    # A, B 방과의 거리 차이가 큰 순서
    teams.sort(key=lambda x: abs(x[1]-x[2]), reverse=True)
    ans = 0
    cnt = {
        'a': a,
        'b': b
    }
    same = []
    for k, dist_a, dist_b in teams:
        if dist_b < dist_a:
            sol(k, 'b', 'a', dist_b, dist_a)
        elif dist_a < dist_b:
            sol(k, 'a', 'b', dist_a, dist_b)
        else:
            same.append((k, dist_a))
    for num, dist in same:
        ans += num * dist

    print(ans)



