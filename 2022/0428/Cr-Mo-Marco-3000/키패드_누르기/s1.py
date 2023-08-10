def solution(numbers, hand):
    l_position = (3, 0)
    r_position = (3, 2)
    my_str = ''
    n = len(numbers)
    my_dict = {1:(0, 0), 4:(1, 0), 7:(2, 0), 3:(0, 2),
               6:(1, 2), 9:(2, 2), 2:(0, 1), 5:(1, 1), 8:(2, 1), 0:(3, 1)}
    for i in numbers:
        if i % 3 == 1:
            my_str += 'L'
            l_position = my_dict[i]
        elif i and not (i % 3):
            my_str += 'R'
            r_position = my_dict[i]
        else:
            num_position = my_dict[i]
            l_dist = abs(num_position[0] - l_position[0]) + abs(num_position[1] - l_position[1])
            r_dist = abs(num_position[0] - r_position[0]) + abs(num_position[1] - r_position[1])
            if l_dist < r_dist:
                my_str += 'L'
                l_position = num_position
            elif l_dist > r_dist:
                my_str += 'R'
                r_position = num_position
            else:
                if hand == 'right':
                    my_str += 'R'
                    r_position = num_position
                else:
                    my_str += 'L'
                    l_position = num_position
    answer = my_str
    return answer


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'
print(solution(numbers, hand))
