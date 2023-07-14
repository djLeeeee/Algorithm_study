def solution(numbers, hand):
    answer = ''
    position_dic = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                    4: (1, 0), 5: (1, 1), 6: (1, 2),
                    7: (2, 0), 8: (2, 1), 9: (2, 2),
                    0: (3, 1)}
    lx, ly = 3, 0
    rx, ry = 3, 2
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            lx, ly = position_dic[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            rx, ry = position_dic[num]
        else:
            x, y = position_dic[num]
            ld = abs(lx - x) + abs(ly - y)
            rd = abs(rx - x) + abs(ry - y)
            if ld < rd:
                answer += 'L'
                lx, ly = x, y
            elif ld > rd:
                answer += 'R'
                rx, ry = x, y
            else:
                if hand == 'left':
                    answer += 'L'
                    lx, ly = x, y
                else:
                    answer += 'R'
                    rx, ry = x, y
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))