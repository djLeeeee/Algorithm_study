def solution(new_id):
    # 1단계 : 소문자 변환
    answer = new_id.lower()
    # 2단계 : 특수문자 소거
    for char in answer:
        if char in '~!@#$%^&*()=+[{]}:?,<>/':
            answer = answer.replace(char, '')
    # 3단계 : 연속된 '.' 변환
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4단계, 5단계 : 처음과 끝의 '.' 제거, 빈 문자열일 때 'a' 추가
    if answer[0] == '.':
        answer = answer[1:]
        if not len(answer):
            answer += 'a'
    if answer[-1] == '.':
        answer = answer[:-1]
        if not len(answer):
            answer += 'a'
    # 6단계, 7단계 : 아이디 길이 조정
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    elif len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]
    return answer



print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("abcdefghijklmn.p"))