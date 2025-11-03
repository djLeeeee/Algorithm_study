import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    tmp = find(parent[x])
    length[x] += length[parent[x]]
    parent[x] = tmp
    return tmp

def union(a, b):
    length[a] = abs(a-b) % 1000
    parent[a] = b

T = int(input())

for _ in range(T):
    n = int(input())
    parent = list(range(n+1))
    length = [0] * (n+1)
    while True:
        command = input().split()
        if command[0] == 'E':
            find(int(command[1]))
            print(length[int(command[1])])
        elif command[0] == 'I':
            union(int(command[1]), int(command[2]))
        else:
            break
