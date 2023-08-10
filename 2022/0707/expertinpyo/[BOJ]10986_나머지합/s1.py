# 순서쌍 구하는 문제라고 생각
# 연속된 부분의 구간합
# 한 점으로 부터 계속 봐야함?
# 해당 점의 각 나머지를 구할 수 있지 않을까
# 한 점에서 끝점까지 읽되, 해당 sum 값이 내 것의 -1을 한 그게 된다면 그렇게 하기

n, m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] %= m
visited = [[] for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i, n):
        if j not in visited[i]:
            if not sum(arr[i:j+1]) % m:
                ans += 1
            elif sum(arr[i:j+1]) % m == arr[i] and len(arr[i:j+1]) != 1:
                visited[i+1].append(j)
                ans += 1
print(ans)