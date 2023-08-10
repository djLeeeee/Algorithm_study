import sys

mod = 10 ** 9 + 7

def do(num, k):
    if k == 1:
        return num
    else:
        half = do(num, k // 2) % mod    # 느낌적인 느낌으로, 어차피 나머지 <= 쪼갠 것들의 나머지?
        if k % 2:                       # 각 단계별로 mod를 해 주어도 상관없는 느낌적인 느낌
            return half * half * num
        else:
            return half * half

input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    if N < 3:
        print(1)
    else:
        print(do(2, N-2) % mod)         # 여기 mod를 한 번 더 나누어 주거나,
                                        # 위에 return에 해주어야 한다.
# 1 => 1 일때 1
# N => 2 일 때 1
# N => 3 일때 2
# N => 4 일때 4
# N => 5 일때 8
# 2 ** (N - 2)
# 규칙 찾는 문제이다
