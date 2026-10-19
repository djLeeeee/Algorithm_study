# Problem: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=5&problemLevel=6&contestProbId=AWDpGfYaAtEDFAUZ&categoryId=AWDpGfYaAtEDFAUZ&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=6&pageSize=10&pageIndex=3
# Submission: 2026-08-27 21:14 / Python / Fail
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    INF = 10 ** 9
    dp = [[INF] * n for _ in range(n)]
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    for i in range(n):
        dp[i][i] = 0
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                tmp = dp[i][k] + dp[k + 1][j] + prefix[j + 1] - prefix[i]
                if tmp < dp[i][j]:
                    dp[i][j] = tmp
    return dp[0][n - 1]
 
 
if __name__ == "__main__":
    for tc in range(int(input())):
        print(f"#{tc + 1} {main()}")
