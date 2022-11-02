import sys
sys.stdin = open('input.txt')

def find(a):
    if parent[a] != a:
        return find(parent[a])
    return a

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
know_list = list(map(int, input().split()))
know_cnt, know = know_list[0], know_list[1:]
parent = [i for i in range(N+1)]

party_cnt = 0
if not know_cnt:
    party_cnt = M
else:
    head = min(know)
    for num in know:
        parent[num] = head
    parties = []
    for _ in range(M):
        party_list = list(map(int, input().split()))
        party_people, party = party_list[0], party_list[1:]
        parties.append(party)
        for j in range(0, len(party) - 1):
            for k in range(j + 1, len(party)):
                union(party[j], party[k])

    true = []
    head_p = find(head)
    for i in range(1, N+1):
        if find(i) == head_p:
            true.append(i)
    for i in range(0, len(parties)):
        flag = True
        for j in range(0, len(parties[i])):
            if parties[i][j] in true:
                flag = False
                break
        if flag:
            party_cnt += 1
print(party_cnt)







