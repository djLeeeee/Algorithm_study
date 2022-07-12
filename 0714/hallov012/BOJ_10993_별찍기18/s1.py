import sys
sys.stdin = open('input.txt')

def star(temp, w, idx):
    if temp == 0:
        return
    h = (w + 1) // 2
    # 홀수라면 삼각형 모양으로 그린다
    if temp % 2:
        for i in range(h):
            data[idx+i][mid+i] = '*'
            data[idx+i][mid-i] = '*'
            data[idx+h-1][mid+i] = '*'
            data[idx+h-1][mid-i] = '*'
        # 바로 다음에 그릴 삼각형은 현재 삼각형의 중앙에 위치해야함
        star(temp-1, (w-1)//2, idx+h//2)
    # 짝수라면 역삼각형
    else:
        for i in range(h):
            data[idx+h-1-i][mid+i] = '*'
            data[idx+h-1-i][mid-i] = '*'
            data[idx][mid+i] = '*'
            data[idx][mid-i] = '*'
        # 바로 다음에 그릴 삼각형은 현재 top 위치의 바로 아래부터 시작
        star(temp-1, (w-1)//2, idx+1)

n = int(input())
x = 1
for _ in range(n-1):
    x = 2*x + 1
y = 2*x - 1
mid = x - 1
data = [[' '] * y for _ in range(x)]
star(n, y, 0)
for i in range(x):
    line = "".join(data[i]).rstrip()
    print(line)



