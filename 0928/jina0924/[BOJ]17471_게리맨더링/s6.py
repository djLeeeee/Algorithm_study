# 백준 17471_게리맨더링 - 통과

import sys
sys.stdin = open('input4.txt')
from itertools import combinations


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


N = int(input())
population = [0] + list(map(int, input().split()))      # 구역 별 인구수
ssum = sum(population)                                  # 모든 인구수 총 합
G = [[0] * (N+1) for _ in range(N+1)]                   # 인접 그래프
for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in range(1, data[0]+1):
        G[i][data[j]] = G[data[j]][i] = 1
result = 1000                                           # 선거구 인구 차이의 최소값을 담을 변수
for i in range(1, N // 2 + 1):                          # 조합을 만들 때 중복 방지를 위해 N//2까지만 조합 생성
    for comb in combinations((range(1, N + 1)), i):
        p = list(range(N+1))                            # 연결 고리의 끝을 담을 리스트(각자 자신으로 초기화)
        group1 = comb
        if len(group1) > 1:                             # group의 원소가 2개 이상이면 연결관계 찾아야함
            for j in range(len(group1)-1):
                for k in range(j+1, len(group1)):
                    if G[group1[j]][group1[k]]:         # 남과 연결되어 있다면
                        union(group1[j], group1[k])     # p에 연결관계 나타내줌
        group2 = list(set(range(1, N + 1)) - set(comb))
        if len(group2) > 1:
            for j in range(len(group2)-1):
                for k in range(j+1, len(group2)):
                    if G[group2[j]][group2[k]]:         # 남과 연결되어 있다면
                        union(group2[j], group2[k])     # p에 연결관계 나타내줌
        for l in range(1, N+1):                         # 마지막으로 find_set 한 번 더 해줘야 진짜 연결관계 나타낼 수 있음
            p[l] = find_set(l)
        if len(set(p)) > 3:                             # 0을 제외하고 그룹이 2개까지만 허용됨 -> 그 이상이면 선거구 못 나눔
            continue
        total1 = 0
        for k in range(len(group1)):
            total1 += population[group1[k]]
        if result > abs(2 * total1 - ssum):             # A + B = X이면 A - B = A - (X - A) = 2A - X
            result = abs(2 * total1 - ssum)
if result == 1000:                                      # result값이 갱신되지 않았다 = 선거구 끝까지 못 나눴다
    result = -1
print(result)