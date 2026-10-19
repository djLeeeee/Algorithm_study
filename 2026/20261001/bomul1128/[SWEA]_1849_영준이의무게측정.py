# Problem: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LeQJqDpwDFAXc
# Submission: 2026-10-14 19:05 / Python / Pass
def main():
    def find(idx):
        if parents[idx] == idx:
            return idx, 0
        past = parents[idx]
        new, ex = find(past)
        parents[idx] = new
        correction[idx] += ex
        return new, correction[idx]
     
    def union(idx, adj, val):
        fi, ci = find(idx)
        fj, cj = find(adj)
        if fi == fj:
            return
        diff = cj + val - ci
        if size[fi] <= size[fj]:
            parents[fi] = fj
            correction[fi] = diff
            size[fj] += size[fi]
        else:
            parents[fj] = fi
            correction[fj] = -diff
            size[fi] += size[fj]
     
    def compare(idx, adj):
        fi, ci = find(idx)
        fj, cj = find(adj)
        if fi != fj:
            return 'UNKNOWN'
        return ci - cj
 
    n, m = map(int, input().split())
    queries = [input() for _ in range(m)]
    result = []
    parents = list(range(n + 1))
    size = [1] * (n + 1)
    correction = [0] * (n + 1)
    for q in queries:
        o, *v = q.split()
        if o == '!':
            x, y, d = map(int, v)
            union(x, y, d)
        elif o == '?':
            x, y = map(int, v)
            result.append(compare(x, y))
    return ' '.join(map(str, result))
 
 
if __name__ == '__main__':
    for tc in range(int(input())):
        res = main()
        print(f"#{tc + 1} {res}")
