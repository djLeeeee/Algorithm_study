n = int(input())
m = int(input())
word = input()
start = 0
result = 0
p_length = 0
while start < m:
    if word[start:start + 3] == 'IOI':
        p_length += 1
        start += 2
    else:
        if p_length >= n:
            result += p_length - n + 1
        start += 1
        p_length = 0
print(result)
