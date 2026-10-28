def main():
    def get_force(idx, mid):
        force = 0
        for j in range(idx + 1):
            force += masses[j] / (mid - points[j]) ** 2
        for j in range(idx + 1, n):
            force -= masses[j] / (mid - points[j]) ** 2
        return force

    n = int(input())
    arr = list(map(int, input().split()))
    points, masses = zip(*sorted(zip(arr[:n], arr[n:])))
    ans = []
    for idx in range(n - 1):
        left = points[idx]
        right = points[idx + 1]
        for _ in range(100):
            mid = (left + right) / 2
            if get_force(idx, mid) > 0:
                left = mid
            else:
                right = mid
        ans.append(f"{(left + right) / 2:.10f}")
    return ' '.join(ans)


if __name__ == '__main__':
    for tc in range(int(input())):
        res = main()
        print(f"#{tc + 1} {res}")
