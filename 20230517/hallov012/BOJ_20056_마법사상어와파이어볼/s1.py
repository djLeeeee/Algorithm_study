import sys
sys.stdin = open('input.txt')
from collections import defaultdict

input = sys.stdin.readline
n, m, k = map(int, input().split())
fire_lst = []
for i in range(m):
    x, y, w, d, s = map(int, input().split())
    fire_lst.append([x-1, y-1, w, d, s])
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(k):
    # 새로운 위치 저장
    new_arr = defaultdict(list)
    for i in range(len(fire_lst)):
        x, y, w, s, d = fire_lst[i]
        nx = (x + s * dx[d]) % n
        ny = (y + s * dy[d]) % n
        new_arr[(nx, ny)].append(i)
    # 결과 저장
    new_fire_lst = []
    for (x, y), lst in new_arr.items():
        if len(new_arr[(x, y)]) > 1:
            w_sum = 0
            s_sum = 0
            d_check = [0, 0]
            for idx in lst:
                w_sum += fire_lst[idx][2]
                s_sum += fire_lst[idx][3]
                d_check[fire_lst[idx][4] % 2] += 1
            if not w_sum // 5:
                continue
            if not d_check[0] or not d_check[1]:
                for nd in [0, 2, 4, 6]:
                    new_fire_lst.append([x, y, w_sum // 5, s_sum // len(lst), nd])
            else:
                for nd in [1, 3, 5, 7]:
                    new_fire_lst.append([x, y, w_sum // 5, s_sum // len(lst), nd])
        else:
            idx = lst[0]
            new_fire_lst.append([x, y, fire_lst[idx][2], fire_lst[idx][3], fire_lst[idx][4]])
    fire_lst = new_fire_lst
ans = 0
for fire in fire_lst:
    ans += fire[2]
print(ans)




