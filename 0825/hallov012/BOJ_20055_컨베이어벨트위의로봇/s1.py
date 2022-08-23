import sys
from collections import deque
sys.stdin = open('input.txt')

n, k = map(int, input().split())
data = deque(list(map(int, input().split())))
robot = deque([0] * n)
ans = 0
while True:
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    data.rotate(1)
    robot.rotate(1)
    # n번째에서 로봇 내리기
    robot[-1] = 0
    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and data[i+1]:
            robot[i+1] = 1
            robot[i] = 0
            data[i+1] -= 1
    robot[-1] = 0
    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if not robot[0] and data[0]:
        robot[0] = 1
        data[0] -= 1
    ans += 1
    #내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다
    if data.count(0) >= k:
        break
print(ans)