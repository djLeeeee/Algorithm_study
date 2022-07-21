string = input()
target = input()
stack = []
for i in range(len(string)):
    stack.append(string[i])
    if string[i] == target[-1] and ''.join(stack[-len(target):]) == target:
        del stack[-len(target):]
if stack:
    print(''.join(stack))
else:
    print("FRULA")