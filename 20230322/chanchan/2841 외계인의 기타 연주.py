# https://www.acmicpc.net/problem/2841
import sys
sys.stdin = open("input/2841.txt")
input = sys.stdin.readline

class Guitar():

    def __init__(self, N, P):
        self.num_flats = P
        self.num_notes = N
        self.notes = {}

    def set_notes(self, n, p):
        temp = self.notes.get(n, [])
        temp.append(p)
        self.notes[n] = temp

    @staticmethod
    def isHigherNote(stack, new_note):
        isHigher = stack[-1] < new_note
        return (isHigher)
    
    @staticmethod
    def isLowerNote(stack, new_note):
        isLower = stack[-1] > new_note
        return (isLower)

    @staticmethod
    def play_note(note):
        stack = []
        cnt = 0
        for n in note:
            # stack이 비어있을 경우
            if (len(stack) == 0):
                stack.append(n)
                cnt += 1
                continue
            
            # 주어진 음이 마지막 음보다 큰 경우
            if (Guitar.isHigherNote(stack, n)):
                stack.append(n)
                cnt += 1

            # 주어진 음이 마지막 음보다 작은 경우
            elif (Guitar.isLowerNote(stack, n)):
                while (stack and stack[-1] > n):
                    stack.pop()
                    cnt += 1
                if (len(stack) == 0 or stack[-1] != n):
                    stack.append(n)
                    cnt += 1
            
            # 주어진 음이 마지막 음과 같은 경우 (그냥 패스)
        return cnt

    def get_min_action(self):
        ans = 0
        for note in self.notes.values():
            ans += self.play_note(note)
        return ans


def solution():
    N, P = map(int, input().split())
    guitar = Guitar(N, P)
    for _ in range(N):
        n, p = map(int, input().split())
        guitar.set_notes(n, p)

    ans = guitar.get_min_action()
    print(ans)

solution()