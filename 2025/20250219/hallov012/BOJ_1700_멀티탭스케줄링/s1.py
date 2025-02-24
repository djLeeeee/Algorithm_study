import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

n, k = map(int, input().split())
item_lst = list(map(int, input().split()))

item_idx_dict = defaultdict(deque)
for idx, item in enumerate(item_lst):
    item_idx_dict[str(item)].append(idx)

# 플러그를 빼야할 때 가장 나중에 사용할 걸 먼저 뺀다
use = []
use_flag = [0] * (k+1)
ans = 0

for item in item_lst:
    if not use_flag[item]:
        if len(use) < n:
            use_flag[item] = 1
            use.append(item)
        else:
            last_use_t = -1
            last_use_item = (0, 0)
            for u_idx, u_item in enumerate(use):
                u_que = item_idx_dict[str(u_item)]
                use_t = u_que[0] if u_que else 101
                if use_t > last_use_t:
                    last_use_t = use_t
                    last_use_item = (u_idx, u_item)
            del use[last_use_item[0]]
            use_flag[last_use_item[1]] = 0

            use.append(item)
            use_flag[item] = 1
            ans += 1

    item_idx_dict[str(item)].popleft()

print(ans)

