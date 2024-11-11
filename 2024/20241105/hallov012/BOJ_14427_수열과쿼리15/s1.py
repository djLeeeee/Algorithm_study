import sys, math
sys.stdin = open('input.txt')

def init(node, start, end):
    if start == end:
        tree[node] = data[start]
    else:
        mid = (start + end) // 2
        tree[node] = min(init(node*2, start, mid), init(node*2+1, mid+1, end))
    return tree[node]

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    if start == end:
        tree[node] = diff
    else:
        mid = (start + end) // 2
        update(node*2, start, mid, idx, diff)
        update(node*2+1, mid+1, end, idx, diff)
        tree[node] = min(tree[node*2], tree[node*2+1])

n = int(input())
nums = list(map(int, input().split()))
data = []
for i in range(n):
    data.append([nums[i], i+1])
tree = [[] for _ in range(pow(2, math.ceil(math.log(n, 2)) + 1))]
init(1, 0, n-1)

m = int(input())
for _ in range(m):
    command = list(map(int, input().split()))
    if len(command) == 1:
        print(tree[1][1])
    else:
        idx = command[1] - 1
        diff = command[2]
        data[idx][0] = diff
        update(1, 0, n-1, idx, data[idx])
