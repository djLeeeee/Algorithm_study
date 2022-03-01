# 0303 

## 숫자 문자열과 영단어 - [프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/81301)

```python
def solution(s):
    transform = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    for key, value in transform.items():
        s = s.replace(key, value)
    return int(s)
```



## 주식 가격 - [프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/42584)

```python
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    for idx, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            i, _ = stack.pop()
            answer[i] = idx - i
        stack.append((idx, price))
    while stack:
        i, _ = stack.pop()
        answer[i] = idx - i
    return answer
```

스택 개념 활용



## 셀프 넘버 - [백준 4673](https://www.acmicpc.net/problem/4673)

```python
def sn(a):
    b=[int(i) for i in str(a)]
    return a+sum(b)  

x=list(range(1,10001))

for i in range(1,10001):
    if sn(i) in x:
        x.remove(sn(i))

for i in x:
    print(i)
```

```python
a = [True] * 10040
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                a[1001 * i + 101 * j + 11 * k + 2 * l] = False
for i in range(10000):
    if a[i] == True:
        print(i)
```

remove 연산이 그렇게 빨리 처리되지는 않을테니, 풀이 방식을 바꿔봤다.



## 신규 아이디 추천 - [프로그래머스](https://www.acmicpc.net/status?from_mine=1&problem_id=4673&user_id=bomul1128)

```python
def solution(new_id):
    new_id = new_id.lower()
    ans = []
    for char in new_id:
        if 'a' <= char <= 'z' or '0' <= char <= '9' or char in '-_.':
            if ans and ans[-1] == '.' and char == '.':
                pass
            else:
                ans.append(char)
    if ans and ans[0] == '.':
        ans.pop(0)
    if not ans:
        ans = ['a']
    if len(ans) >= 16:
        ans = ans[:15]
    if ans and ans[-1] == '.':
        ans.pop()
    if len(ans) <= 2:
        while len(ans) < 3:
            ans += ans[-1]
    return ''.join(ans)
```

하라는 대로 차근차근 해주기