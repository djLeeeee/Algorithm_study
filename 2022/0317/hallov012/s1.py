import sys
sys.stdin = open('input.txt')

def fine_sit(g_idx, p_num):
    while 1:
        p, visited = case.pop(0)
        now_visited = visited[:]
        if p == p_num:
            case.append([p, now_visited])
            break
        i, j = 0, 0     # i: 왼쪽으로 이동, j: 오른쪽으로 이동
        if not now_visited[g_idx]:
            now_visited[g_idx] = 1
            case.append([p+1, now_visited])
        else:
            while 0 <= g_idx - i and now_visited[g_idx - i] != 0:
                if 0 < g_idx - i:
                    i += 1
                    if not g_idx - i:
                        i = n
            while g_idx + j < n + 2 and now_visited[g_idx + j] != 0:
                if g_idx + j < n + 1:
                    j += 1
                    if g_idx + j == n + 1:
                        j = n
            if i < j:
                now_visited[g_idx - i] = i + 1
                case.append([p + 1, now_visited])
            elif i > j:
                now_visited[g_idx + j] = j + 1
                case.append([p + 1, now_visited])
            else:
                if p < p_num - 1:
                    now_visited[g_idx - i] = i + 1
                    now_visited[g_idx + j] = j + 1
                    case.append([p + 2, now_visited])
                else:
                    now_visited[g_idx - i] = i + 1
                    case.append([p + 1, now_visited])
                    new_visited = visited[:]
                    new_visited[g_idx + j] = j + 1
                    case.append([p + 1, new_visited])


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    gate = [list(map(int, input().split())) for _ in range(3)]
    case = [[0, [0] * (n + 2)]]
    order = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    ans = n ** 2
    for i in range(len(order)):
        case = [[0, [0] * (n + 2)]]

        g_idx, p_num = gate[order[i][0]]
        fine_sit(g_idx, p_num)
        for j in range(len(case)):
            case[j][0] = 0

        g_idx_1, p_num_1 = gate[order[i][1]]
        fine_sit(g_idx_1, p_num_1)
        for k in range(len(case)):
            case[k][0] = 0

        g_idx_2, p_num_2 = gate[order[i][2]]
        fine_sit(g_idx_2, p_num_2)

        for a in range(len(case)):
            cnt = sum(case[a][1])
            if cnt < ans:
                ans = cnt
    print(f'#{tc} {ans}')


