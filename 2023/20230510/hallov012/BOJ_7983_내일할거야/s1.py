import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
assignments = [list(map(int, input().split())) for _ in range(n)]
assignments.sort(key=lambda x:x[1])
# 첫 과제 제출일 - 소요일이 기본 값
ans = assignments[0][1] - assignments[0][0]
# 과제 중간에 쉬는 날이 있었는지
save = 0

for i in range(1, n):
    d, t = assignments[i]
    # 이전 과제를 제출하고 바로 시작했을 때의 값 - 이번 과제 제출일
    gab = (assignments[i-1][1] + d) - t
    # 더 빨리 시작해야한다
    if gab > 0:
        if gab > save:
            ans -= gab - save
            save = 0
        else:
            save -= gab
    # 과제 사이에 텀이 있었으면 save로 저장함
    else:
        save -= gab

print(ans)