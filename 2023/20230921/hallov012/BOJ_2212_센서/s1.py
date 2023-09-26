import sys
sys.stdin = open('input.txt')

n = int(input())
k = int(input())
sensors = sorted(list(map(int, input().split())))
ans = 0
if k >= n:
    print(0)
    exit()

dist = []
for i in range(1, n):
    dist.append(sensors[i] - sensors[i-1])
dist.sort()
# k개의 센서는 이미 수신할 수 있으니 나머지 n-k 개의 길이 만큼 수신 가능하게 하면 됨
print(sum(dist[:n-k]))
