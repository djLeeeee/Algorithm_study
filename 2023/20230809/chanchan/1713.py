# https://www.acmicpc.net/problem/1713
import sys
sys.stdin = open("./input/1713.txt")
input = sys.stdin.readline
# ----------------------------------------
class Student:
    sequence = 0
    def __init__(self):
        self.sequence = Student.sequence
        Student.sequence += 1
        self.cnt = 1

def set_data(num, records):
    student = records[num]
    student.cnt += 1

def set_new_data(num, frames):
    records[num] = Student()
    frames.append(num)

def sort_data(frames, records):
    frames.sort(key = lambda stu:(-records[stu].cnt, -records[stu].sequence))
# ----------------------------------------
limit = int(input())
N = int(input())


frames = []
records = {}
nums = list(map(int, input().split()))
for num in nums:
    if len(frames) >= limit:
        if num in frames:
            set_data(num, records)
        else:
            prev_num = frames.pop()
            records[prev_num].cnt = 0
            set_new_data(num, frames)
    else:
        try:
            set_data(num, records)
        except KeyError:
            set_new_data(num, frames)

    sort_data(frames, records)
    
print(*sorted(frames))