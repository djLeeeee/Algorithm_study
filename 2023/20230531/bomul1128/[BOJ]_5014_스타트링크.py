# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/5014
f, s, g, u, d = map(int, input().split())
visited = [-1] * (f + 1)
stack = []
visited[s] = 0
stack.append(s)
for now in stack:
    if now == g:
        break
    if now + u <= f and visited[now + u] == -1:
        visited[now + u] = visited[now] + 1
        stack.append(now + u)
    if now - d > 0 and visited[now - d] == -1:
        visited[now - d] = visited[now] + 1
        stack.append(now - d)
if visited[g] == -1:
    print("use the stairs")
else:
    print(visited[g])
