import sys
sys.stdin = open('input.txt')

T = int(input())
# 에라스토테네스의 체 구현
nums = [True]*10001
nums[0], nums[1] = False, False
for i in range(2, 101):
    for j in range(2, len(nums)//i):
        nums[i*j] = False
# print(nums)
for _ in range(T):
    n = int(input())
    # 결과값 담을 리스트
    result = []
    # 중간값까지 체에서 두 숫자가 모두 true면
    for idx in range(n//2 + 1):
        if nums[idx] and nums[n-idx]:
            # 두 값의 차의 절댓값과, 두 숫자를 튜플로 만들어서 결과값에 추가
            result.append((abs(idx-n+idx), idx, n-idx))
    # 첫번째 값을 기준으로 정렬되기 때문에 여기서 첫번째 요소를 선택하면 됨
    # result = sorted(result)
    # 두 값의 체를 제외하고 프린트!
    print(result[-1][1], result[-1][2])
