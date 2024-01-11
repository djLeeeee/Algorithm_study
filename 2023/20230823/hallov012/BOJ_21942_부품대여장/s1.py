import sys
from collections import defaultdict
from datetime import datetime, timedelta
sys.stdin = open('input.txt')

input = sys.stdin.readline

def l_convert(l):
    day = int(l.split('/')[0])
    hour, minute = map(int, l.split('/')[1].split(':'))
    return timedelta(days=day, hours=hour, minutes=minute)

def time_convert(date, time):
    year, month, day = map(int, date.split('-'))
    hour, minute = map(int, time.split(':'))
    return datetime(year, month, day) + timedelta(hours=hour, minutes=minute)


n, l, f = input().split()
n, f = int(n), int(f)
l = l_convert(l)

rent_dict = defaultdict(list)
fine_dict = defaultdict(int)

for _ in range(n):
    date, time, part, name = input().split()
    now = time_convert(date, time)

    type_name = " ".join((part, name))
    if not rent_dict[type_name]:
        rent_dict[type_name].append(now + l)
    else:
        return_time = rent_dict[type_name][0]
        del rent_dict[type_name]

        if return_time < now:
            late = now - return_time
            day = late.days
            fine = (day * 24 * 60 + late.seconds // 60) * f
            fine_dict[name] += fine


if not fine_dict:
    print(-1)
else:
    ans = sorted(fine_dict.items())
    for line in ans:
        print(*line)



