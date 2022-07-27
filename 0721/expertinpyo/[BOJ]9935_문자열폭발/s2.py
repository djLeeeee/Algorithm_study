string = input()
target = input()
stack = []
for i in range(len(string)):
    if string[i] == target[0]:
        stack.append(i)
while stack:
    idx = stack.pop()
    if string[idx:idx+len(target)] == target:
        string = string[:idx] + string[idx+len(target)::]
if string:
    print(string)
else:
    print("FRULA")