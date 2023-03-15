# https://www.acmicpc.net/problem/14891
import sys
sys.stdin = open("input/14891.txt")
input = sys.stdin.readline

class Gear():
    def __init__(self, info, number):
        # n번째 기어
        self.number = number
        # [9시 방향 notch index, 12시 방향 notch index, 3시 방향 notch index]
        self.notches = [6, 0, 2]
        # gear의 자석 정보
        self.info = list(map(int, info.rstrip()))

    def spin(self, way, vst):
        vst[self.number] = 1
        left = self.number - 1
        right = self.number + 1

        # 조건 1) 0번째 기어까지 있으므로 | 조건 2) 해당 기어를 방문하지 않았다면
        if (0 <= left and not vst[left]):
            my_magnet = self.info[self.notches[0]]
            side_gear = gears[left]
            side_magnet = side_gear.info[side_gear.notches[2]]
            if (my_magnet != side_magnet):
                # 좌우 기어의 노치가 서로 다른 극의 자석이라면 해당 기어 반대 방향으로 spin
                side_gear.spin(way * -1, vst)
        
        # 조건 1) 3번째 기어까지 있으므로 | 조건 2) 해당 기어를 방문하지 않았다면
        if (right < 4 and not vst[right]):
            my_magnet = self.info[self.notches[2]]
            side_gear = gears[right]
            side_magnet = side_gear.info[side_gear.notches[0]]
            if (my_magnet != side_magnet):
                # 좌우 기어의 노치가 서로 다른 극의 자석이라면 해당 기어 반대 방향으로 spin
                side_gear.spin(way * -1, vst)
            
        self.move_gear(way)

    
    def move_gear(self, way):
        for ind in range(3):
            self.notches[ind] = (self.notches[ind] - way) % 8


gears = [Gear(input(), ind) for ind in range(4)]

for _ in range(int(input())):
    gear_num, way = map(int, input().split())
    vst = [0] * 4
    gears[gear_num - 1].spin(way, vst)
    

ans = 0
for num in range(4):
    gear = gears[num]
    top_notch = gear.notches[1]
    ans += (gear.info[top_notch] == 1) * (2 ** num)

print(ans)