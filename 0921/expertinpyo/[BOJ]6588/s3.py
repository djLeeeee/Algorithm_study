num = []
while True:
    n = int(input())
    if not n:
        break
    num.append(n)

n = max(num)
nums = [True] * (n+1)
prime_number = []
for i in range(2, int(n**0.5)+1):
    if nums[i]:
        if i % 2:
            prime_number.append(i)
        for j in range(2*i, n+1, i):
            nums[j] = False
for n in num:
    for prime in prime_number :
        if nums[prime] and nums[n-prime]:
            print(f"{n} = {prime} + {n-prime}")
            break
    else:
        print("Goldbach's conjecture is wrong.")