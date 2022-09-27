import sys
sys.stdin = open('input.txt')

def find(cnt):
    global ans
    if cnt == n:
        check = 0
        for i in range(n-1):
            check += abs(temp[i]-temp[i+1])
        ans = max(ans, check)
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            temp.append(nums[i])
            find(cnt+1)
            temp.pop()
            visited[i] = 0


n = int(input())
nums = list(map(int, input().split()))
ans = 0
visited = [0] * n
temp = []
find(0)
print(ans)