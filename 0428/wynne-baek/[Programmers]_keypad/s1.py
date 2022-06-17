def check_distance(c, left, right):
    distance_left = abs(left[0] - c) + abs(left[1] - 1)
    distance_right = abs(right[0] - c) + abs(right[1] - 1)
    if distance_left > distance_right:
        return 'R'
    elif distance_left < distance_right:
        return 'L'
    else:
        return False


def solution(numbers, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]
    left_num = [1, 4, 7]
    right_num = [3, 6, 9]
    center_num = [2, 5, 8, 0]
    for number in numbers:
        # 1, 4, 7
        if number in left_num:
            answer += 'L'
            a = left_num.index(number)
            left = [a, 0]
        # 3, 6, 9
        elif number in right_num:
            answer += 'R'
            b = right_num.index(number)
            right = [b, 2]
        # 2, 5, 8, 0
        else:
            c = center_num.index(number)
            # 좌우 거리 비교(함수 호출)
            result = check_distance(c, left, right)
            # 거리에 차이가 있으면
            if result:
                answer += result
            # 거리에 차이가 없으면 어느 손잡이인지 비교
            else:
                if hand == 'right':
                    answer += 'R'
                elif hand == 'left':
                    answer += 'L'
            if answer[-1] == 'L':
                left = [c, 1]
            elif answer[-1] == 'R':
                right = [c, 1]
    return answer