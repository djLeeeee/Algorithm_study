import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
know = list(map(int, input().split()))
know_check = [0] * (n+1)
# 진실을 알고있는 사람 체크
for i in range(1, len(know)):
    know_check[know[i]] = 1

# 한 사람이 참석하는 모든 파티를 저장 (key: 사람, value: 참석하는 파티들)
person = defaultdict(list)
# 파티와 참석자 정보를 저장
parties = []
for i in range(m):
    party = list(map(int, input().split()))
    parties.append(party[1:])
    for p in party[1:]:
        person[p].append(i)

# que에는 진실을 알고 있는 사람의 번호를 저장
que = deque(know[1:])
# 진실을 말하는 파티 => 1, 거짓을 말하는 파티 => 0
ans = [1] * m
while que:
    know_p = que.popleft()
    # 진실을 알고있는 사람이 참석하는 파티
    for party in person[know_p]:
        # 진실을 말해야하므로 ans를 0으로 바꿈
        if ans[party]:
            ans[party] = 0
        # 진실을 말하는 파티에 참석하는 모든 사람들은 진실을 알게된다
        for p in parties[party]:
            if not know_check[p]:
                know_check[p] = 1
                que.append(p)

print(sum(ans))