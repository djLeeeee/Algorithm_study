def solution(places):
    answer = [1] * 5
    for i in range(5):
        case = places[i]
        person = []
        for a in range(5):
            for b in range(5):
                if case[a][b] == 'P':
                    person.append([a, b])
        check_case = []
        for a in range(len(person)):
            for b in range(a+1, len(person)):
                x1, y1 = person[a]
                x2, y2 = person[b]
                d = abs(x1-x2) + abs(y1-y2)
                if d <= 2:
                    check_case.append([person[a], person[b]])
        if not check_case:
            continue
        for check in check_case:
            x1, y1 = check[0]
            x2, y2 = check[1]
            if x1 == x2:
                if case[x1][y1+1] != 'X':
                    answer[i] = 0
            elif y1 == y2:
                if case[x1+1][y1] != 'X':
                    answer[i] = 0
            elif x2 == x1+1 and y2 == y1+1:
                if case[x1+1][y1] != 'X' or case[x1][y1+1] != 'X':
                    answer[i] = 0
            elif x2 == x1+1 and y2 == y1-1:
                if case[x1][y1-1] != 'X' or case[x1+1][y1] != 'X':
                    answer[i] = 0
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
