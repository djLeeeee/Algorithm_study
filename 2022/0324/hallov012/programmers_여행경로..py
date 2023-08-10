from collections import deque
import copy

def solution(tickets):
    answer = []
    dic = {}
    for ticket in tickets:
        if ticket[0] not in dic.keys():
            dic[ticket[0]] = [ticket[1]]
        else:
            dic[ticket[0]].append(ticket[1])
    for key in dic.keys():
        dic[key].sort()
    root = ['ICN']
    que = deque([['ICN', root, dic]])
    while que:
        start, new_root, new_dic = que.popleft()
        if len(new_root) == len(tickets) + 1:
            answer = new_root
            break
        # 출발 경로가 없는 도착지로만 존재 할 경우 dic에서 key를 찾을 수 없기 때문에 key가 dic에 있다는 가정을 넣어주어야 한다
        if start in new_dic and new_dic[start]:
            for end in new_dic[start]:
                now_dic = copy.deepcopy(new_dic)
                now_dic[start].remove(end)
                now_root = copy.deepcopy(new_root)
                now_root.append(end)
                que.append([end, now_root, now_dic])

    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "COO"]]))