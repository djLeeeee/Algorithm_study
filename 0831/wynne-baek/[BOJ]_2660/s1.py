import sys
sys.stdin = open('input.txt')
from collections import defaultdict, deque

def bfs(num):
    queue = deque([[num, 0]])
    while queue:
        other, cnt = queue.popleft()
        score[num][other-1] = min(score[num][other-1], cnt)
        # other의 친구 queue에 추가
        other_friend = connect[other]
        for f in other_friend:
            if score[num][f-1] == 51:
                queue.append([f, cnt + 1])


N = int(input())
score = [[51 for _ in range(N)] for _ in range(N+1)]
connect = defaultdict(list)
while True:
    A, B = map(int, input().split())
    if A == -1 and B == -1:
        break
    else:
        connect[A].append(B)
        connect[B].append(A)
for i in range(1, N+1):
    bfs(i)
#print(score)
real_score = []
for i in range(1, N+1):
    real_score.append(max(score[i]))
# print(real_score)
lowest = min(real_score)
candidate = []
for i in range(1, N+1):
    if lowest == max(score[i]):
        candidate.append(i)
print(lowest, len(candidate))
print(*candidate)