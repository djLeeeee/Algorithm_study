def solution(s):
    answer = ''
    temp = ''
    for char in s:
        if char in numbers:
            answer += char
        else:
            #임시에 추가하고
            temp += char
            #문자열 비교
            if temp in number:
                #인덱스 가져와서 추가해주고
                answer += str(number.index(temp))
                #임시 변수 비워주기
                temp = ''
    return int(answer)

number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers = ['0', '1', '2','3','4','5','6','7','8','9']