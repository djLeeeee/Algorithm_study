num = []
while True:
    n = int(input())
    if not n:
        break
    num.append(n)
n = max(num)
nums = [True] * (n+1)
for i in range(2, int(n**0.5)+1):
    if nums[i]:
        for j in range(2*i, n+1, i):
            nums[j] = False
for n in num:
    for i in range(3, n, 2):
        if nums[i] and nums[n-i]:
            print(f"{n} = {i} + {n-i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")