import sys
sys.stdin = open("input/18116.txt")
input = sys.stdin.readline

def solution():
    N = int(input())
    parents = [-1 for _ in range(pow(10, 6) + 1)]

    def get_top_node(num):
        if parents[num] >= 0:
            parent = get_top_node(parents[num])
            parents[num] = parent
            return parent
        else:
            return num

    def make_it_same(nums):
        num1, num2 = map(int, nums)
        num1 = get_top_node(num1)
        num2 = get_top_node(num2)
        if num1 == num2:
            return
        
        A, B = (num1, num2) if parents[num1] < parents[num2] else (num2, num1)
        parents[A] += parents[B]
        parents[B] = A

    for _ in range(N):
        order, *nums = input().split()
        if order == "I":
            make_it_same(nums)

        elif order == "Q":
            top = get_top_node(int(nums[0]))
            print(parents[top] * -1)
solution()