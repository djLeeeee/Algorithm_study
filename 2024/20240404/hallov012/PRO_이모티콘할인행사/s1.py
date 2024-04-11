def solution(users, emoticons):
    answer = [0, 0]
    n, m = len(users), len(emoticons)
    sales = [0] * m

    def check():
        nonlocal answer
        temp = [0, 0]
        for s_sale, s_cost in users:
            cost = 0
            for i in range(m):
                if sales[i] >= s_sale:
                    cost += emoticons[i] * (100 - sales[i]) // 100
            if cost >= s_cost:
                temp[0] += 1
            else:
                temp[1] += cost

        if temp[0] > answer[0]:
            answer = temp
        elif temp[0] == answer[0]:
            answer[1] = max(temp[1], answer[1])
        return

    def find(idx):
        if idx == m:
            check()
            return
        for i in range(1, 5):
            sales[idx] = i * 10
            find(idx+1)

    find(0)
    return answer

datas = [
    [[[40, 10000], [25, 10000]], [7000, 9000]],
    [[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]]
]

for u, e in datas:
    print(solution(u, e))