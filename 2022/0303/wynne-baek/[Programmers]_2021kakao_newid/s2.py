def solution(new_id):
    temp = ''
    temp2 = ''
    allowed = 'abcdefghijgklmnopqrstuvwxyz1234567890-_.'
    #lower(new_id)
    for char in new_id:
        # 1단계, 소문자로 치환
        if char.isupper() is True:
            temp += char.lower()
        else:
            temp += char
    #special(temp)
    for char in temp:
        if char in allowed:
            temp2 += char
    #one_dot(temp)
    temp = ''
    for char in temp2:
        if char == '.':
            if len(temp) > 0 and temp[-1] != '.':
                temp += char
        else:
            temp += char
    #delete_dot(temp)
    if len(temp) > 0 and temp[0] == '.':
        temp = temp[1:]
    if len(temp) > 0 and temp[-1] == '.':
        temp = temp[:-1]
    #new_id_empty(new_id)
    if len(temp) == 0:
        temp = 'a'
    #longer_than_16(new_id)
    if len(temp) > 15:
        temp = temp[:15]
        while temp[-1] == '.':
            temp = temp[:-1]
    #shorter_than_2(new_id)
    if len(temp) <= 2:
        while len(temp) != 3:
            temp += temp[-1]
    return temp



import sys
sys.stdin = open('input.txt')
for _ in range(5):
    new_id = str(input())
    print(solution(new_id))
