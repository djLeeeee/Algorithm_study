"""
학생 N명
친구의 친구는 친구다.
가장 적은 비용으로 모든 사람과 친구

입력:
N, M, k = 학생 수, 친구관계 수, 가지고 있는 돈
[N개의 숫자] : 각 학생이 원하는 친구비
M개의 줄에 v w : v - w 연결되어 있음(양방향)
친구로 만드는 최소 비용을 구해서
다 사귈 수 있으면 최소비용, 사귈 수 없으면 'Oh no' 출력
"""
import sys
sys.stdin = open('input.txt')

def find(n):
    if reps[n] != n:
        reps[n] = find(reps[n])
    return reps[n]

# 두 개의 집합을 합치는 함수
def union(node1, node2):
    rep1 = find(node1)
    rep2 = find(node2)
    if rep2 != rep1:
        if fee[rep2] < fee[rep1]:
            reps[rep1] = rep2
        else:
            reps[rep2] = rep1

N, M, k = map(int, input().split())
fee = [0] + list(map(int, input().split()))
reps = [i for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

check = set()
pay = 0
for i in range(1, N+1):
    a = find(i)
    if a in check:
        continue
    else:
        check.add(a)
        pay += fee[a]
if pay <= k:
    print(pay)
else:
    print('Oh no')