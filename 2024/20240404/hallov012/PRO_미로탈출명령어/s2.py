def solution(n, m, x, y, r, c, k):
    answer = ''

    short = abs(x-r) + abs(y-c)
    x, y, r, c = x-1, y-1, r-1, c-1

    if k < short or (k-short) % 2:
        return 'impossible'

    while k > abs(x-r) + abs(y-c):
        k -= 1
        if x < n-1:
            x += 1
            answer += 'd'
        elif y > 0:
            y -= 1
            answer += 'l'
        else:
            y += 1
            answer += 'r'

    x_gab, y_gab = r-x, c-y
    if x_gab >= 0:
        answer += 'd' * x_gab
    if y_gab < 0:
        answer += 'l' * abs(y_gab)
    if y_gab >= 0:
        answer += 'r' * y_gab
    if x_gab < 0:
        answer += 'u' * abs(x_gab)
    return answer

print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))