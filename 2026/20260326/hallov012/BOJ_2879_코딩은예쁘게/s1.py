import sys
sys.stdin = open('input.txt')

def check_value(target, d, idx):
    if not target or target[-1][1] == idx-1:
        target.append((d, idx))
        return True
    else:
        return False

def run(arr, p_flag):
    global ans, flag
    flag = True
    val = min(x for x, _ in arr)
    ans += val
    if not p_flag:
        val *= -1
    for _, y in arr:
        diff[y] -= val

n = int(input())
tabs = list(map(int, input().split()))
c_tabs = list(map(int, input().split()))

diff = [c_tabs[i] - tabs[i] for i in range(n)]

ans = 0

while True:
    left, right = [], []
    flag = False
    for i in range(n):
        if not diff[i]:
            pass
        d = diff[i]
        if d > 0:
            if not check_value(left, d, i):
                run(left, True)
                left = [(d, i)]
        elif d < 0:
            d = abs(d)
            if not check_value(right, d, i):
                run(right, False)
                right = [(d, i)]
    if left:
        run(left, True)
    if right:
        run(right, False)
    if not flag:
        break
print(ans)
