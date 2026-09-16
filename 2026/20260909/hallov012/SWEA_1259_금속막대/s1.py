import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    rods = []
    next_rod = {}
    female = set()

    for i in range(n):
        m, f = nums[2*i], nums[2*i+1]
        rods.append((m, f))
        next_rod[m] = f
        female.add(f)

    start = None
    for m, f in rods:
        if m not in female:
            start = m
            break

    ans = []

    cur = start
    while cur in next_rod:
        next = next_rod[cur]
        ans.append(cur)
        ans.append(next)
        cur = next

    print(f"#{tc}", *ans)

