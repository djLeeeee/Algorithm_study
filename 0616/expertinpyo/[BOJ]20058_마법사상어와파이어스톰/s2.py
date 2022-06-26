# 축이 생긴다고 생각해보기
# 현재 좌표 기준으로 기준을 넘어가면 마이너스, 기준 전이면 플러스
#
def fire(n):
    if not n:
        return
    for k in range(4**(N-n)):
        # k번의 격자 존재
        trial = k % (2**n)
        for i in range(1)


di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
spells = list(map(int, input().split()))

for spell in spells:
    alternative = [[0] * (2 ** N) for _ in range(2 ** N)]
    arr = fire(spell)
print(arr)