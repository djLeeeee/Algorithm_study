import sys
sys.stdin = open('input.txt')

def nums_oper(a, b, oper):
    if oper == '+':
        return a+b
    elif oper == '-':
        return a-b
    elif oper == '*':
        return a*b

def dfs(idx, cnt):
    global ans
    # 마지막이면 ans 갱신
    if idx == n-1:
        ans = max(ans, cnt)
    # 연산자, 숫자가 뒤에 남아 있으면 지금까지 나온걸 괄호로 묶고 연산
    if idx + 2 < n:
        dfs(idx+2, nums_oper(cnt, int(s[idx+2]), s[idx+1]))
    # 뒤에 연산이 더 많으면 뒤를 묶고 그 결과랑 같이 연산
    if idx + 4 < n:
        tmp = nums_oper(int(s[idx+2]), int(s[idx+4]), s[idx+3])
        dfs(idx+4, nums_oper(cnt, tmp, s[idx+1]))

n = int(input())
s = input().rstrip()
ans = -sys.maxsize
dfs(0, int(s[0]))
print(ans)