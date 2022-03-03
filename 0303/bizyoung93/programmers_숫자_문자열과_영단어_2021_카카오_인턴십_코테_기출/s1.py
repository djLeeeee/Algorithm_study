# 지독한 정답
def solution(s):
    i = 0
    my_string = ''
    while i < len(s):
        if s[i] == 'z':  # zero
            my_string += '0'
            i += 3
        elif s[i] == 'o':  # one
            my_string += '1'
            i += 2
        elif s[i] == 't':  # two three
            if s[i + 1] == 'w':
                my_string += '2'
                i += 2
            else:
                my_string += '3'
                i += 4
        elif s[i] == 'f':  # four five
            if s[i + 1] == 'o':
                my_string += '4'
                i += 3
            else:
                my_string += '5'
                i += 3
        elif s[i] == 's':  # six seven
            if s[i + 1] == 'i':
                my_string += '6'
                i += 2
            else:
                my_string += '7'
                i += 4
        elif s[i] == 'e':  # eight
            my_string += '8'
            i += 4
        elif s[i] == 'n':  # nine
            my_string += '9'
            i += 3
        else:
            my_string = my_string + s[i]
        i += 1

    answer = int(my_string)
    return answer


print(solution("one4seveneight"))