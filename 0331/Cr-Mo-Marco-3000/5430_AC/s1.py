import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(sys.stdin.readline().rstrip())


for tc in range(1, T+1):
    order = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline().rstrip())
    my_deque = deque(sys.stdin.readline().rstrip())
    my_deque.popleft()
    my_deque.pop()
    # direction이 0이면 정방향 1이면 역방향
    # d는 첫 번째 수를 버리는 것, 즉 direction이 0이면 popleft, 1이면 pop

    direction = 0
    error = 0
    for i in order:
        # R이면 direction을 반대로 바꿔줌
        if i == 'R':
            direction = (direction + 1) % 2
        elif i == 'D':                                  # D면 숫자들을 삭제해준다.
            if not my_deque:                            # 덱이 빈 상태면
                print('error')                          # error를 출력하고 플래그를 1로 만들어준 후
                error = 1
                break                                   # break 해준다
            elif direction:                             # 역방향이면
                while my_deque and my_deque[-1] != ',': # 쉼표가 나올 때까지 빼주다가
                    my_deque.pop()
                if my_deque:                            # 루프가 끝났는데 덱이 있으면 쉼표때문에 빠져나왔다는 뜻이므로
                    my_deque.pop()                      # 쉼표까지 빼 준다
            elif not direction:                         # 정방향이면
                while my_deque and my_deque[0] != ',':  # 마찬가지로 동작해 준다.
                    my_deque.popleft()
                if my_deque:
                    my_deque.popleft()


    if error:                                           # 에러가 출력되었다면 아래 출력을 수행하지 않는다.
        continue
    else:
        if not my_deque:                                # 에러가 출력되지 않았는데 덱이 비었다면 '[]' 출력
            print('[]')
        elif direction:
            print('[', end='')
            temp = "".join(my_deque)
            a = deque(map(int, temp.split(',')))
            for i in range(len(a)-1, 0, -1):
                print(a[i], end='')
                print(',', end='')
            print(a[0], end='')
            print(']')
        elif not direction:
            print('[', end='')
            temp = "".join(my_deque)
            a = deque(map(int, temp.split(',')))
            for i in range(0, len(a)-1):
                print(a[i], end='')
                print(',', end='')
            print(a[-1], end='')
            print(']')
