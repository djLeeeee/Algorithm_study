# Problem: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=5&problemLevel=6&contestProbId=AXNQOb3avD0DFAXS&categoryId=AXNQOb3avD0DFAXS&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=6&pageSize=10&pageIndex=2
# Submission: 2026-08-27 22:01 / Python / Pass
def main():
    n, p = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = p + 1
    left = 0
    for right in range(n):
        while arr[right] - arr[left] - (right - left) > p:
            left += 1
        tmp = right - left + 1 + p 
        if tmp > ans:
            ans = tmp
    return ans
 
 
if __name__ == "__main__":
    for tc in range(int(input())):
        print(f"#{tc + 1} {main()}")
