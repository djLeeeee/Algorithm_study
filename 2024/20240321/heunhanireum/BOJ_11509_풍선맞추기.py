import sys
sys.stdin = open("input.txt")

N = int(input())
balloon = list(map(int, input().split()))
height = [0]*1000001
height[balloon[0]] = 1
for b in balloon:
    if height[b] > 0:
        height[b-1] += 1
        height[b] -= 1
    else:
        height[b-1] += 1
print(sum(height))