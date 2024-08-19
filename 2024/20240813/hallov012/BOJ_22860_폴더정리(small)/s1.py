import sys
from collections import defaultdict
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(tmp, target):
    p_type, p_cnt = set(), 0
    tmp.append(target)
    for (item, isFolder) in dir[target]:
        if isFolder:
            find(tmp, item)
            tmp.pop()
            p_type.update(f_dict[item][0])
            p_cnt += f_dict[item][1]
        else:
            p_type.add(item)
            p_cnt += 1
    root = '/'.join(tmp)
    r_dict[root] = [len(p_type), p_cnt]
    f_dict[target] = [p_type, p_cnt]

n, m = map(int, input().split())
dir = defaultdict(list)
for _ in range(n+m):
    P, F, C = input().split()
    dir[P].append((F, int(C)))
f_dict = {}
r_dict = {}

find([], 'main')

Q = int(input())
for _ in range(Q):
    query = input().strip()
    print(*r_dict[query])