import sys
sys.stdin = open('input.txt')

def find_bracket(str):
    bracket = []
    for char in Q:
        if char == '(':
            bracket.append(char)
        elif char == ')':
            if bracket and bracket[-1] == '(':
                bracket.pop()
            else:
                print('NO')
                return False
    return bracket

T = int(input())
for i in range(T):
    Q = input()
    bracket = find_bracket(Q)
    if bracket == False:
        continue
    elif bracket:
        print('NO')
    elif bracket == []:
        print('YES')