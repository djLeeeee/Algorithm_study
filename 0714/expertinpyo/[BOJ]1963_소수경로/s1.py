# 본인의 제곱근 까지 나눠봐서 소수인지 판별
# 그 이후 bfs 진행

from collections import deque

def isPrime(x):
    for n in range(2, int(x**0.5)+1):
        if not x % n:
            return False
    return True

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    queue = deque([a])
    visited = [0] * 9000    # 1000의 자리 숫자만 보면 되므로
    nothing = True
    while queue:
        a = queue.popleft()
        if a == b:
            print(visited[a-1000])
            nothing = False
            break
        for i in range(4):
            m = a // (10 ** (i+1))
            r = a % (10 ** i)
            for j in range(10):
                value = m * 10 ** (i+1) + r + j * 10 ** i
                if 1000 <= value < 10000 and not visited[value-1000] and value != a and isPrime(value):
                    visited[value-1000] = visited[a-1000] + 1
                    queue.append(value)
    if nothing:
        print("Impossible")