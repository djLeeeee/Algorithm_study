import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
chars = [input().rstrip() for _ in range(n)]
left, right = 0, n-1
ans = ''
while left <= right:
    if chars[left] > chars[right]:
        ans += chars[right]
        right -= 1
    elif chars[left] < chars[right]:
        ans += chars[left]
        left += 1
    else:
        # 나중에 나올 단어가 사전순으로 더 앞에 있는 애들을 출력
        l, r = left, right
        flag = 0
        while l <= r:
            if chars[l] < chars[r]:
                flag = 1
                break
            elif chars[l] > chars[r]:
                flag = 2
                break
            l += 1
            r -= 1
        if flag == 1 or flag == 0:
            ans += chars[left]
            left += 1
        elif flag == 2:
            ans += chars[right]
            right -= 1

cnt = 0
for char in ans:
    print(char, end="")
    cnt += 1
    if not cnt % 80:
        print()
