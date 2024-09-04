import sys
sys.stdin = open('input.txt')

def find(a_lst, b_lst, common):
    if not a_lst or not b_lst:
        return common
    max_a, max_b = max(a_lst), max(b_lst)
    idx_a, idx_b = a_lst.index(max_a), b_lst.index(max_b)
    if max_a == max_b:
        common.append(max_a)
        return find(a_lst[idx_a+1:], b_lst[idx_b+1:], common)
    else:
        if max_a > max_b:
            a_lst.pop(idx_a)
        else:
            b_lst.pop(idx_b)
        return find(a_lst, b_lst, common)

n = int(input())
a_lst = list(map(int, input().split()))
m = int(input())
b_lst = list(map(int, input().split()))

ans = find(a_lst, b_lst, [])
print(len(ans))
print(*ans)

