# 백준 10216번 Count Circle Groups

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())                            # 테스트 케이스 수
for tc in range(T):
    N = int(input())                        # N: 적군 진영의 숫자
    p = [i for i in range(N)]               # 부모를 담을 배열
    data = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        x1, y1, r1 = data[i]                # 현재 위치를 기준으로
        for j in range(i + 1, N):           # 그 이후 진영들 전부 돌면서
            x2, y2, r2 = data[j]
            if (x1 - x2) **2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2:    # 영역이 겹친다면 직접 통신이 가능한 지역
                union(i, j)
    for i in range(1, N):                   # 최종적으로 한 바퀴 돌면서 부모 찾아줌
        find_set(i)
    print(len(set(p)))