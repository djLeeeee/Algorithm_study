def solution(new_id):

    # 1단계
    new_id = new_id.lower()

    # 2단계 3단계
    # 처음에는 한 번에 하려고 했는데, 그렇게 푸는 게 아니더라, 단계별로 해야 한다.
    i = 0
    while i < len(new_id):
        if not new_id[i].isalpha() and not new_id[i].isdecimal() and not new_id[i] == '-' and not new_id[i] == '_' and not new_id[i] == '.':
            new_id = new_id.replace(new_id[i], '')
            continue
        i += 1

    # 3단계
    i = 0
    while i < len(new_id):
        if i < (len(new_id) - 1) and new_id[i] == new_id[i + 1] == '.':
        # 문자열 관련 함수는, 단순 검증이 아닌 이상 반환!
            new_id = new_id[0:i] + new_id[i+1:]
            continue
        i += 1

    # 4단계
    if len(new_id) and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5단계
    if not new_id:
        new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    while len(new_id) < 3:
        new_id = new_id + new_id[-1]
    return new_id

answer = solution('abcdefghijklmn.p')
print(answer)