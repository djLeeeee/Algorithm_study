def main():
    def get_code(row, idx):
        res = []
        for _ in range(8):
            counts = [0, 0, 0]
            for j, v in enumerate('101'):
                while idx >= 0 and row[idx] == v:
                    counts[j] += 1
                    idx -= 1
            scale = min(counts)
            key = tuple(cnt // scale for cnt in reversed(counts))
            res.append(patterns[key])
            while idx >= 0 and row[idx] == '0':
                idx -= 1
        return tuple(reversed(res)), idx

    patterns = {
        (2, 1, 1): 0,
        (2, 2, 1): 1,
        (1, 2, 2): 2,
        (4, 1, 1): 3,
        (1, 3, 2): 4,
        (2, 3, 1): 5,
        (1, 1, 4): 6,
        (3, 1, 2): 7,
        (2, 1, 3): 8,
        (1, 1, 2): 9,
    }
    n, m = map(int, input().split())
    rows = set(input().strip() for _ in range(n))
    codes = set()
    for raw in rows:
        row = bin(int(raw, 16))[2:].rstrip('0')
        idx = len(row) - 1
        while idx >= 0:
            code, idx = get_code(row, idx)
            codes.add(code)
    ans = 0
    for code in codes:
        if (sum(code[::2]) * 3 + sum(code[1::2])) % 10 == 0:
            ans += sum(code)
    return ans


if __name__ == '__main__':
    for tc in range(int(input())):
        res = main()
        print(f"#{tc + 1} {res}")
