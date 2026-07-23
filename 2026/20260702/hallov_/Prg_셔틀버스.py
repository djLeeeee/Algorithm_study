def get_time_num(time_str):
    hour, min = map(int, time_str.split(':'))
    return 60 * hour + min

def solution(n, t, m, timetable):
    answer = ''
    crew = []
    for time in timetable:
        crew.append(get_time_num(time))
    crew.sort()

    b_time = 9 * 60
    idx = 0
    for i in range(n):
        cnt = 0
        while idx < len(crew) and crew[idx] <= b_time and cnt < m:
            idx += 1
            cnt += 1
        if i == n-1:
            if cnt < m:
                answer = b_time
            else:
                answer = crew[idx-1] - 1
        b_time += t
    return f"{answer // 60:02d}:{answer % 60:02d}"

input_lst = [
    [1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]],
    [2, 10, 2, ["09:10", "09:09", "08:00"]]
]

for a, b, c, d in input_lst:
    print(solution(a, b, c, d))