import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

ans = 1
for i in range(n):
    # ans는 이 다음번에 측정해보려는 값이며 ans-1까지는 모두 측정 가능함
    # 왜? ans-1까지 모두 측정 가능할 때, i번째 숫자가 ans보다 작거나 같기만 하면
    # nums[i]를 단일로 사용하거나, ans-nums[i]를 만들었던 이전 조합을 사용해서 만들 수 있음
    if ans >= nums[i]:
        ans += nums[i]
    # 근데 만약 nums[i] > ans라면 ans라는 값은 만들 수 없는 값으로 남게 됨
    else:
        break
print(ans)