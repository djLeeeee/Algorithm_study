import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
start = {}
for i in range(n):
    data = input().rstrip()
    start[data] = i

end = []
for _ in range(n):
    data = input().rstrip()
    end.append(data)

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        # i번째로 나온 차가 뒤에 나온 차들보다 늦게 들어갔을 경우엔 추월했다고 판단
        if start[end[i]] > start[end[j]]:
            ans += 1
            break

print(ans)