import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find():
    cnt = {
        'X': 0,
        'O': 0,
        '.': 0
    }
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2]:
            cnt[arr[i][0]] += 1
    for j in range(3):
        if arr[0][j] == arr[1][j] == arr[2][j]:
            cnt[arr[0][j]] += 1
    if row[0] == row[4] == row[8]:
        cnt[row[0]] += 1
    if row[2] == row[4] == row[6]:
        cnt[row[2]] += 1
    return cnt['X'], cnt['O']

while True:
    row = list(input().rstrip())
    if len(row) == 3:
        break
    x_cnt = row.count('X')
    o_cnt = row.count('O')
    ans = False
    arr = [row[i*3: (i+1)*3] for i in range(3)]
    if x_cnt - o_cnt > 1 or o_cnt > x_cnt: # 순서상 불가능
        pass
    else:
        x_t, o_t = find()
        if x_cnt == o_cnt:  # O가 마지막
            ans = o_t and not x_t
        elif x_cnt == o_cnt + 1:  # x가 마지막이거나 승부가 안난 경우
            if x_cnt == 5:
                ans = not o_t
            else:
                ans = x_t and not o_t
    print('valid' if ans else 'invalid')


