# Problem: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWH0J5T6BZwDFAVB
# Submission: 2026-10-14 18:17 / Python / Pass
def main():
    def split(limit):
        splitted = []
        cnt = 0
        for v in arr:
            if v <= limit:
                cnt += 1
            elif cnt > 0:
                splitted.append(cnt)
                cnt = 0
        if cnt:
            splitted.append(cnt)
        return splitted
 
    def is_ok(splitted):
        si = ti = 0
        sl = len(splitted)
        while ti < k and si < sl:
            t = target[ti]
            s = splitted[si]
            if s >= t:
                splitted[si] -= t
                ti += 1
            else:
                si += 1
        return si < sl
 
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    target = list(map(int, input().split()))
    left = 1
    right = max(arr)
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if is_ok(split(mid)):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
 
 
if __name__ == '__main__':
    for tc in range(int(input())):
        res = main()
        print(f"#{tc + 1} {res}")
