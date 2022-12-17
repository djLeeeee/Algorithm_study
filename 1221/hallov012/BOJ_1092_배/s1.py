import sys
sys.stdin = open('input.txt')

n = int(input())
weight = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
weight.sort(reverse=True)
box.sort(reverse=True)
if box[0] > weight[0]:
    print(-1)
    exit()

ans = 0
while box:
    ans += 1
    for i in range(n):
        for j in range(len(box)):
            if weight[i] >= box[j]:
                box.pop(j)
                break

print(ans)
