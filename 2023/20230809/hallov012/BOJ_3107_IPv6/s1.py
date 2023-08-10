import sys
sys.stdin = open('input.txt')

data = input().split('::')
str_data = ''
if len(data) == 2:
    if data[0] == '':
        l = data[1].count(':') + 1
        str_data = '0000:' * (8-l) + data[1]
    elif data[1] == '':
        l = data[0].count(':') + 1
        str_data = data[0] + ':0000' * (8-l)
    else:
        l = data[0].count(':') + data[1].count(':') + 2
        str_data = data[0] + ':0000' * (8-l) + ':' + data[1]
else:
    str_data = data[0]

str_lst = str_data.split(':')
for i in range(8):
    if len(str_lst[i]) != 4:
        str_lst[i] = '0' * (4-len(str_lst[i])) + str_lst[i]

ans = ':'.join(str_lst)
print(ans)