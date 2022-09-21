# 6588 골드바흐의 추측
# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다
# 백만 이하의 모든 짝수에 대해 이 추측 검증
num = []
while True:
    n = int(input())
    if not n:
        break
    num.append(n)
n = max(num)
nums = [True] * (n+1)
sosu = []

for i in range(2, n+1):
    if nums[i]:
        if i % 2:
            sosu.append(i)
        for j in range(2*i, n+1, i):
            if nums[j]:
                nums[j] = False
print(sosu)
for n in num:
    for i in range(len(sosu)):
        if sosu[i] > n:
            right = i - 1
            break
    else:
        right = i
    left = 0
    ans = False
    while left <= right:
        print(sosu[left], sosu[right])
        if sosu[left] + sosu[right] > n:
            right -= 1
        elif sosu[left] + sosu[right] == n:
            ans = f"{n} = {sosu[left]} + {sosu[right]}"
            break
        else:
            left += 1
            right = i - 1
    if not ans:
        ans = "Goldbach's conjecture is wrong."
    print(ans)
