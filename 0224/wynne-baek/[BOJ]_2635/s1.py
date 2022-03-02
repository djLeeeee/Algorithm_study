import sys
sys.stdin = open('input.txt')

def number(N, K):
    global cnt
    if N - K < 0:
        return cnt
    elif N - K >= 0:
        C = N - K
        answer.append(C)
        cnt += 1
        number(K, C)

N = int(input())
max_cnt = 0
max_list = []
#N도 두번째에 올 수 있다! 야 너두 할 수 있어!
for i in range(1, N+1):
    answer = [N, i]
    cnt = 2
    number(N, i)
    if cnt > max_cnt:
        max_cnt = cnt
        max_list = answer
print(max_cnt)
print(*max_list)