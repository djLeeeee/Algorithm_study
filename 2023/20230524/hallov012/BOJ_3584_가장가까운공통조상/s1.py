import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    p = [0] * (n+1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        p[b] = a
    A, B = map(int, input().split())
    target_a = [A]
    target_b = [B]
    while p[A]:
        target_a.append(p[A])
        A = p[A]
    while p[B]:
        target_b.append(p[B])
        B = p[B]
    # 제일 위의 노드까지 target에 저장되어 있으니 역순으로 내려오면서 부모노드 확인
    lv_a = len(target_a) - 1
    lv_b = len(target_b) - 1
    while target_a[lv_a] == target_b[lv_b]:
        lv_a -= 1
        lv_b -= 1
    print(target_a[lv_a + 1])