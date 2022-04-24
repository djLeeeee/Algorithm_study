import sys
sys.stdin = open('input.txt')

def primelist(num):
    arr = [True] * (num+1)
    arr[0], arr[1] = False, False
    m = int(num ** 0.5)
    for i in range(2, m+1):
        if arr[i] == True:
            for j in range(i+i, N+1, i):
                arr[j] = False
    return arr

M, N = map(int, sys.stdin.readline().split())
arr = primelist(N)
for idx in range(M, N+1):
    if arr[idx] == True:
        print(idx)

# 제곱근까지만 검사하는 방법
# def Prime(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True
#
# M, N = map(int, input().split())
# for i in range(M, N+1):
#     if Prime(i):
#         print(i)

#완전탐색
# import sys
#
# M, N = map(int, input().split())
# for num in range(M, N+1):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num)