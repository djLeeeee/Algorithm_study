# 백준 15903번 카드 합체 놀이 - 204ms

import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline

n, m = map(int, input().split())            # n: 카드 개수, m: 합체 횟수
cards = list(map(int, input().split()))
for _ in range(m):
    cards.sort()
    x, y = cards[0], cards[1]               # 가장 작은 값 두 개 뽑아서 더해야 최종 결과 가장 작게 나옴
    cards[0] = cards[1] = x + y
print(sum(cards))