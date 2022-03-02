def lower(new_id):
    temp = ''
    for char in new_id:
        # 1단계, 소문자로 치환
        if char.isupper() is True:
            temp += char.lower()
        else:
            temp += char
    return temp

def special(new_id):
    temp = ''
    for char in new_id:
        if char not in '!@#*':
            temp += char
    return temp

def one_dot(new_id):
    temp = ''
    for char in new_id:
        if char == '.':
            if temp[-1] != '.':
                temp += char
        else:
            temp += char
    return temp

def delete_dot(new_id):
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    return new_id

def new_id_empty(new_id):
    if new_id == '':
        new_id = 'a'
    return new_id

def longer_than_16(new_id):
    if len(new_id) > 15:
        new_id = new_id[:16]
        while new_id[-1] == '.':
            new_id = new_id[:-1]
    return new_id

def shorter_than_2(new_id):
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id