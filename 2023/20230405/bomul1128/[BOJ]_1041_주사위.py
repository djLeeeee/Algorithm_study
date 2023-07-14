n = int(input())
a, b, c, d, e, f = map(int, input().split())
if n == 1:
    print(a + b + c + d + e + f - max(a, b, c, d, e, f))
else:
    corner = 4
    edge = 8 * n - 12
    center = 4 * (n - 1) * (n - 2) + (n - 2) ** 2
    corner_val = min(
        a + b + c,
        a + b + d,
        a + c + e,
        a + d + e,
        f + b + c,
        f + b + d,
        f + c + e,
        f + d + e
    )
    edge_val = min(
        a + b,
        a + c,
        a + d,
        a + e,
        f + b,
        f + c,
        f + d,
        f + e,
        b + c,
        b + d,
        c + e,
        d + e
    )
    center_val = min(a, b, c, d, e, f)
    print(corner * corner_val + edge * edge_val + center * center_val)
