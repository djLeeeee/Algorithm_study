import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

ans = 0
for i in range(n-2):
    l, r = i+1, n-1
    k = -nums[i]
    checked_idx = n
    while l < r:
        tmp = nums[l] + nums[r]
        # i번째 학생을 넣어서 0점을 만들 수 있는 경우
        if tmp == k:
            # 이 다음 애들의 점수가 모두 같으면 뒤에 i, l, (나머지 r번 까지의 애들)로 조합을 짤 수 있음
            if nums[l] == nums[r]:
                ans += r - l
            else:
                if checked_idx > r:
                    checked_idx = r
                    # r번째 애들과 점수가 같은 애들 중 가장 작은 번호를 찾아냄
                    # i, l, (현재 r번째 애들과 같은 점수를 가진 애들)로 조합을 짤 수 있음
                    while checked_idx >= 0 and nums[checked_idx-1] == nums[r]:
                        checked_idx -= 1
                ans += r - checked_idx + 1
            l += 1
        # 점수를 더 키워야 함
        elif tmp < k:
            l += 1
        else:
            r -= 1

print(ans)

