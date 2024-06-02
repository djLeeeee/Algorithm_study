import sys
sys.stdin = open('input.txt')

N = int(input())
nlst = sorted(map(int, input().split()))
if N < 3:
    print(0)
else:
    cnt = 0
    for i in range(N):
        num = nlst[i]
        left, right = 0, N-1
        while left < right:
            if nlst[left]+nlst[right] < num or left == i:
                left += 1
            elif nlst[left]+nlst[right] > num or right == i:
                right -= 1
            elif nlst[left]+nlst[right] == num:
                cnt += 1
                break
    print(cnt)