# Problem: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWErcQmKy6kDFAXi
# Submission: 2026-10-14 17:26 / Python / Pass
def main():
    n, m = map(int, input().split())
    hate_bits_list = [0] * n
    for _ in range(m):
        x, y = map(int, input().split())
        if x > y:
            x, y = y, x
        hate_bits_list[y - 1] |= 1 << (x - 1)
    entry = [0, 1]
    for i in range(1, n):
        hate_bits = hate_bits_list[i]
        ex = 1 << i
        for j in range(len(entry)):
            bit = entry[j]
            if bit & hate_bits:
                continue
            entry.append(bit | ex)
    return len(entry)
 
 
if __name__ == '__main__':
    for tc in range(int(input())):
        res = main()
        print(f"#{tc + 1} {res}")
