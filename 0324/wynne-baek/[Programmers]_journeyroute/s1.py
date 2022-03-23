# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# tickets = [["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]
# tickets = [['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]
# tickets = [['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'], ['A', 'C']]
tickets = [['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]

def solution(tickets):
    answer = []
    can_go = dict()
    for ticket in tickets:
        x, y = ticket[0], ticket[1]
        #출발지
        if x not in can_go.keys():
            can_go[x] = [y]
        elif x in can_go.keys():
            can_go[x].append(y)
        if y not in can_go.keys():
            can_go[y] = []
    for key in can_go.keys():
        can_go[key].sort()
    stack = ['ICN']
    while stack:
        temp = stack[-1]
        if not can_go[temp]:
            answer.append(stack.pop(0))
        else:
            stack.append(can_go[temp].pop())
    # answer.reverse()
    return answer

print(list(solution(tickets)))