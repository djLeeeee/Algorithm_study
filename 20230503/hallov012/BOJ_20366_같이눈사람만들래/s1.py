import sys
sys.stdin = open('input.txt')

n = int(input())
h_lst = sorted(list(map(int, input().split())))
ans = sys.maxsize
# 한 눈사람은 i, j번째로 만든다
for i in range(n):
    for j in range(i+3, n):
        # 나머지 눈사람은 left, right 번째로 만든다
        left, right = i + 1, j - 1
        while left < right:
            temp = (h_lst[i] + h_lst[j]) - (h_lst[left] + h_lst[right])
            if ans > abs(temp):
                ans = abs(temp)
                if ans == 0:
                    print(0)
                    exit()
            # 첫번째 눈사람의 크기가 더 작다 => 두번째 눈사람의 크기를 줄인다
            if temp < 0:
                right -= 1
            # 두번째 눈사람의 크기가 더 작다 => 두번째 눈사람의 크기를 키운다
            else:
                left += 1
print(ans)



