import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, l, k = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(k)]

# 모든 x, y 조합을 좌상단의 점으로 생각해서 나머지 별들이 몇개 들어가는지 확인
cnt = 0
for x, _ in stars:
    for _, y in stars:
        tmp = 0
        for a, b in stars:
            if x <= a <= x+l and y <= b <= y+l:
                tmp += 1
        cnt = max(cnt, tmp)

print(k-cnt)