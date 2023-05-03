# https://www.acmicpc.net/problem/7511
import sys
sys.stdin = open("./input/7511.txt")
input = sys.stdin.readline

def get_top_parent(parents, num):
    if (parents[num] != num):
        parents[num] = get_top_parent(parents, parents[num])
    return parents[num]

def set_parent(parents, num1, num2):
    n1, n2 = get_top_parent(parents, num1), get_top_parent(parents, num2)
    if (n1 < n2):
        parents[n2] = n1
    else:
        parents[n1] = n2

for test_case in range(1, int(input()) + 1):
    num_users = int(input())
    parents = [i for i in range(num_users)]

    for _ in range(int(input())):
        a, b = map(int, input().split())
        if get_top_parent(parents, a) != get_top_parent(parents, b):
            set_parent(parents, a, b)
    
    print(f"Scenario {test_case}:")
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if get_top_parent(parents, a) != get_top_parent(parents, b):
            print(0)
        else:
            print(1)
    print()