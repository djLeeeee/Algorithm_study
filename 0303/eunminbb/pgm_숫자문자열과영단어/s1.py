def solution(s):
    answer = ''
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    each = ''
    for char in s:
        if char.isdigit():      # 숫자일 경우
            answer += char
        else:                   # 문자일 경우
            each += char
            for num in word:
                if num == each:
                    answer += str(word.index(num))
                    each = ''       # each 초기화

    return int(answer)