from collections import defaultdict
import sys
sys.stdin = open('input.txt')

# defaultdict 활용
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_dict = defaultdict(int)
for letter in letters:
    letters_dict[letter]
# 입력
cnt = int(input())
numbers = []
for _ in range(cnt):
    numbers.append(input())
for number in numbers:
    expo = len(number)-1
    for char in number:
        letters_dict[char] += 10 ** expo
        expo -= 1
nums_list = sorted(letters_dict.values(), reverse=True)[:9]
result = 0
idx = 0
for i in range(9, 0, -1):
    result += nums_list[idx] * i
    idx += 1
print(result)

