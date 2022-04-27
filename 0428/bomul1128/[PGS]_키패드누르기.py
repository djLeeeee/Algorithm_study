def solution(numbers, hand):
    pad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    def middle(target, l, r):
        x, y = pad[target]
        lx, ly = pad[l]
        rx, ry = pad[r]
        if abs(lx - x) + abs(ly - y) > abs(rx - x) + abs(ry - y):
            return 'R'
        if abs(lx - x) + abs(ly - y) < abs(rx - x) + abs(ry - y):
            return 'L'
        if hand == 'left':
            return 'L'
        return 'R'

    left = '*'
    right = '#'
    answer = ''
    for number in numbers:
        if number in {1, 4, 7}:
            left = number
            answer += 'L'
        elif number in {3, 6, 9}:
            right = number
            answer += 'R'
        else:
            if middle(number, left, right) == 'L':
                answer += 'L'
                left = number
            else:
                answer += 'R'
                right = number
    return answer
