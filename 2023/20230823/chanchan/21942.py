# https://www.acmicpc.net/problem/21942
import sys
sys.stdin = open("./input/21942.txt")
input = sys.stdin.readline

from datetime import datetime
import time as TIME
# ----------------------------------------

def get_limit(L):
    limit = 0
    day, time = L.split("/")
    limit += int(day) * 24 * 60
    hh, mm = map(int, time.split(":"))
    limit += hh * 60 + mm
    return limit

def get_min(date, time):
    fmt = "%Y-%m-%d %H:%M"
    date_datetime = datetime.strptime(f'{date} {time}', fmt)
    date_milisec = TIME.mktime(date_datetime.timetuple())
    return int(date_milisec / 60)
    
# ----------------------------------------
data = {}
answer = {}

N, L, F = input().rstrip().split()
LIMIT = get_limit(L)

for _ in range(int(N)):
    date, time, part, name = input().rstrip().split()
    
    data[name] = data.get(name, {})
    date_min = get_min(date, time)

    person = data[name]
    if (part in person):
        rental_time = person[part]
        gap = date_min - rental_time
        if (gap > LIMIT):
            answer[name] = answer.get(name, 0) + int(F) * (gap - LIMIT)
    else:
        person[part] = date_min
    
    
if len(answer) == 0:
    print(-1)
else:
    for key in sorted(answer):
        print(f'{key} {answer[key]}')
