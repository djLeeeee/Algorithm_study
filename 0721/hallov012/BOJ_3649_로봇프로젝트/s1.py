import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        data = [int(input()) for _ in range(n)]
        data.sort()
        ans = []
        left, right = 0, n-1
        flag = False
        while left < right:
            temp = data[left] + data[right]
            # 제일 작은 수, 제일 큰 수에서 한 칸씩 전진하며 비교하므로 제일 먼저 나온 ans 값이 둘 사이의 차이가 가장 크다
            if temp == x:
                print(f'yes {data[left]} {data[right]}')
                flag = True
                break
            elif temp > x:
                right -= 1
            else:
                left += 1

        if not flag:
            print('danger')
    except:
        break