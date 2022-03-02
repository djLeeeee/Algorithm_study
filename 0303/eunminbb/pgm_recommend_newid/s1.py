#테케 23 런타임에러ㅜㅜ

def dot(lst):
    for i in range(len(lst)-1):
        if lst[i] == '.':
            if lst[i+1] == '.':
                lst.pop(i+1)
                return dot(lst)
    return


def solution(new_id):

    new_id = new_id.lower()
    new_lst = list(new_id)
    # 2.
    a = 0
    while a < len(new_lst):
        if new_lst[a].isalpha() or new_lst[a].isdigit() or new_lst[a] in ['-', '_', '.']:
            a += 1
        else:
            new_lst.pop(a)
    # 3.
    dot(new_lst)

    # 4.
    if len(new_lst) >= 2:
        for k in [0, -1]:
            if new_lst[k] == '.':
                new_lst.pop(k)
    elif len(new_lst) == 1:
        if new_lst[0] == '.':
            new_lst.pop()

    if not new_lst:
        new_lst.append('a')

    if len(new_lst) >= 16:
        new_lst = new_lst[:15]
        if new_lst[-1] == '.':
            new_lst.pop()

    elif len(new_lst) <= 2:
        while len(new_lst) < 3:
            new_lst.append(new_lst[-1])
    # elif len(new_lst) == 2:
    #     new_lst.append(new_lst[-1])
    # elif len(new_lst) == 1:
    #     new_lst = new_lst*3

    answer = ''.join(new_lst)
    return answer

