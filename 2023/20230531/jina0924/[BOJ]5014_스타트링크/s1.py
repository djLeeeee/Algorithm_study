# 백준 5014번 스타트링크

import sys
sys.stdin = open('input.txt')

f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)
visited[s] = 1
queue = [s]
for v in queue:
    if v == g:
        print(visited[v] - 1)
        break
    vu, vd = v + u, v - d
    if vu <= f and not visited[vu]:
        queue.append(vu)
        visited[vu] = visited[v] + 1
    if vd > 0 and not visited[vd]:
        queue.append(vd)
        visited[vd] = visited[v] + 1
else:
    print('use the stairs')