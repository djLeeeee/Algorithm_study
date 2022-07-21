import sys
input = sys.stdin.readline
while True:
    try:
        N = int(input().strip()) * 10000000
        array = []
        K = int(input().strip())
        array = [int(input().strip()) for _ in range(K)]
        array.sort()
        right = K - 1
        left = 0
        while left <= right:
            v = array[left] + array[right]
            if v == N:
                if left != right:
                    print('yes', array[left], array[right])
                elif left == right:
                    print('danger')
                break
            elif v > N:
                right -= 1
            elif v < N:
                left += 1
        else:
            print('danger')
    except ValueError or EOFError:
        break

# 처음에는 readline으로 가지 말고 그냥 input을 써야 하나? 했는데 시간초과 뜨는 걸 보니 그것도 아니고
# 뒤에 strip()을 붙이면 안 되나? 된다?
# 문제 푸는 컨셉은 쉽게 떠올렸는데 Try Error 처리 과정에서 오답이 났다.
# try, except 문을 쓸 때는 전부를 try 안에 넣어 주어야 하는 부분에서 틀린 게 맞나보다