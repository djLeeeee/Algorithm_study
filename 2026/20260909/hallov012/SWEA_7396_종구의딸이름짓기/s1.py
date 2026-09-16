import sys
sys.stdin = open('s_input.txt')

T = int(input())

def check_next(nx, ny):
    global min_char
    if not (0 <= nx < n and 0 <= ny < m):
        return
    char = arr[nx][ny]
    if char < min_char:
        min_char = char
        next.clear()
        next.append((nx, ny))
    elif char == min_char:
        next.append((nx, ny))
    return

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input().strip() for _ in range(n)]

    cur = [(0, 0)]
    ans = [arr[0][0]]

    for _ in range(n+m-2):
        min_char = 'z'
        next = []
        for x, y in cur:
            check_next(x+1, y)
            check_next(x, y+1)
        ans.append(min_char)
        cur = list(set(next))

    print(f"#{tc} {''.join(ans)}")

