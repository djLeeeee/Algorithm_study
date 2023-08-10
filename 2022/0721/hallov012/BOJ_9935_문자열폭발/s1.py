import sys
sys.stdin = open('input.txt')

word = input()
bomb = input()
stack = []
for char in word:
    stack.append(char)
    # char가 bomb의 마지막 문자와 같을 때, stack의 마지막 char을 bomb와 비교
    # 왜 마지막 단어랑 비교해주는가? => 폭발이 일어나도 마지막 단어들만 비교하며 바로 처리해줄 수 있기 때문에 앞에서부터 다시 순회할 필요가 없음
    if char == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]
ans = ''.join(stack)

if ans == '':
    print('FRULA')
else:
    print(ans)
