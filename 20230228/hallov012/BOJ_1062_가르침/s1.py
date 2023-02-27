import sys
sys.stdin = open('input.txt')

def dfs(idx, cnt):
    global ans
    if cnt == k:
        temp = 0
        for word in words:
            for char in word:
                if not visited[char]:
                    break
            else:
                temp += 1
        ans = max(ans, temp)
        return
    for i in range(idx+1, 26):
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1)
            visited[i] = 0

input = sys.stdin.readline

n, k = map(int, input().split())
words = [[] for _ in range(n)]
for i in range(n):
    word = input().rstrip()
    for char in word:
        words[i].append(ord(char)-97)

if k < 5:
    print(0)
    exit()
know = {(ord(char)-97) for char in 'antic'}
ans = 0
chars = set(range(26)) - know
visited = [0] * 26
for char in know:
    visited[char] = 1

dfs(-1, 5)

print(ans)
