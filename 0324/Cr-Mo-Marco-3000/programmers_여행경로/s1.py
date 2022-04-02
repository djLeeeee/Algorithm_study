def solution(tickets):
    N = len(tickets)
    my_set = set()
    my_dict = {}

    # 알파벳 순으로, 딕셔너리를 만들어 주기 위한 전처리, set => list => sort
    for i in range(N):
        for j in range(2):
            my_set.add(tickets[i][j])
    my_list = list(my_set)
    my_list.sort()

    for i in range(1, len(my_list) + 1):
        my_dict[my_list[i-1]] = i

    V = len(my_dict)
    g = [[] for _ in range(V+1)]
    # 뀨











    # return answer



tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets_2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

solution(tickets)
# solution(tickets_2)