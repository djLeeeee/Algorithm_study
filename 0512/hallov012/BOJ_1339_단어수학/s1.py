import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
alpa = defaultdict(int)
str_list = [input().strip() for _ in range(n)]
for str in str_list:
    for i in range(len(str)-1, -1, -1):
        alpa[str[i]] += 10 ** (len(str)-i-1)   # 딕셔너리에 '알파벳: 배당된 수가 1일 때의 값' 형태로 저장
sort_alpa = sorted(alpa.items(), key=lambda x: x[1], reverse=True) # 1을 배정받았을 때 얻을 수 있는 값이 가장 큰 것부터 정렬
alpa_dic = {}
m = 9
for i in range(len(sort_alpa)):
    char, num = sort_alpa[i]
    if char not in alpa_dic.keys(): # 더 높은 값을 얻을 수 있는 수부터 값을 할당
        alpa_dic[char] = m
        m -= 1
ans = 0
for i in range(len(sort_alpa)):
    char, num = sort_alpa[i]
    ans += alpa_dic[char] * num
print(ans)
