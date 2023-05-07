import sys
sys.stdin = open('input.txt')

word = input().rstrip()
n = len(word)
stack = []
target = ['P', 'P', 'A', 'P']
for i in range(n):
    stack.append(word[i])
    if stack[-4:] == target:
        for _ in range(3):
            stack.pop()
if stack == target or stack == ['P']:
    print('PPAP')
else:
    print('NP')
