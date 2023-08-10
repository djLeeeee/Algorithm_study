def check(num):
    for c in str(num):
        if c in broken:
            return False
    return True


n = int(input())
m = int(input())
if m:
    broken = list(input().split())
else:
    broken = []
result = abs(n - 100)
for i in range(1000000):
    if check(i) and result > abs(i - n) + len(str(i)):
        result = abs(i - n) + len(str(i))
print(result)
