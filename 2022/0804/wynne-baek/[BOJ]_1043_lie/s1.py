import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
know_list = list(map(int, input().split()))
know_cnt, know = know_list[0], know_list[1:]
parent = [i for i in range(N+1)]
parent[0] = 1
party_parent = [0] * M
if know_cnt:
    for num in know:
        parent[num] = "True"
party_cnt = 0
parties = []
for _ in range(M):
    party_list = list(map(int, input().split()))
    party_people, party = party_list[0], party_list[1:]
    parties.append(party)
    temp = [parent[num] for num in party]
    if "True" in temp:
        for num in party:
            parent[num] = "True"
    else:
        for num in party:
            parent[num] = "False"
print(parent)
print(parties)
for idx in range(len(parties)):
    temp2 = [parent[num] for num in parties[idx]]
    if "True" in temp2:
        continue
    else:
        party_cnt += 1
print(party_cnt)




