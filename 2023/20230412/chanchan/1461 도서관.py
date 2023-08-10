# https://www.acmicpc.net/problem/1461
import sys
sys.stdin = open("./input/1461.txt")
input = sys.stdin.readline

# 세준이의 위치 = 0
# 마구놓은 책 위치 = 0

N, M= map(int, input().split())

books = list(map(int, input().split()))
neg = []
pos = []

for book in books:
    if book > 0:
        pos.append(book)
    elif book < 0:
        neg.append(-1 * book)
neg.sort()
pos.sort()

def set_back(arr, cnt):
    tot = arr[-1]
    while cnt > 0 and arr:
        arr.pop()
        cnt -= 1
    return tot

answer = 0
flag = 0
if neg and pos:
    if (neg[-1] > pos[-1]):
        flag = 1
elif neg:
    flag = 1

if flag:
    answer += set_back(neg, M)
else:
    answer += set_back(pos, M)
while pos:
    answer += 2 * set_back(pos, M)
while neg:
    answer += 2 * set_back(neg, M)

print(answer)