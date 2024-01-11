import sys
sys.stdin = open('input.txt')

S = input()
cnt = 0
open = close = 0
for char in S:
    if char == '(':
        open += 1
        cnt += 1
    else:
        close += 1
        cnt -= 1
    # cnt == 0 이면 거기까진 완전한 괄호니까 그 안에 있는 요소를 삭제하면 안된다
    if cnt == 0:
        open = 0
    # cnt < 0 이 되면 안된다 :)
    elif cnt < 0:
        print(close)
        break
else:
    print(open)

