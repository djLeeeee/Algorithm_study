def solution(new_id):
    new_id = new_id.lower()
    ans = []
    for char in new_id:
        if 'a' <= char <= 'z' or '0' <= char <= '9' or char in '-_.':
            if ans and ans[-1] == '.' and char == '.':
                pass
            else:
                ans.append(char)
    if ans and ans[0] == '.':
        ans.pop(0)
    if not ans:
        ans = ['a']
    if len(ans) >= 16:
        ans = ans[:15]
    if ans and ans[-1] == '.':
        ans.pop()
    if len(ans) <= 2:
        while len(ans) < 3:
            ans += ans[-1]
    return ''.join(ans)
    