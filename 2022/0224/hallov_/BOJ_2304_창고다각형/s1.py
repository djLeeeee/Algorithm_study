import sys
sys.stdin = open('input.txt')

n = int(input())
dic = {}
for _ in range(n):
    data = list(map(int, input().split()))
    dic[data[0]] = data[1]
sort_dic = sorted(dic.items()) # (l, h)의 형태로 l 정렬
cnt = 0
max_h = max(dic.values())
h = sort_dic[0][1]
l = sort_dic[0][0]
i = 0
while h != max_h:
    if sort_dic[i+1][1] > h:
        cnt += (max_h - h) * (sort_dic[i+1][0] - l)
        h = sort_dic[i+1][1]
        l = sort_dic[i+1][0]
    i += 1
h = sort_dic[-1][1]
l = sort_dic[-1][0] + 1
j = 1
while h != max_h:
    if h < sort_dic[n-j-1][1]:
        cnt += (max_h - h) * (l - sort_dic[n-j-1][0]-1)
        h = sort_dic[n-j-1][1]
        l = sort_dic[n-j-1][0] + 1
    j += 1
total = max_h * (sort_dic[-1][0] - sort_dic[0][0] + 1)
print(total-cnt)
