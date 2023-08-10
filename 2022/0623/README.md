# 0623 알고리즘 스터디



> 마지막 스터디 문제 백준 18291번은 수업 시간에 잘 다루지 않은 분할 정복 개념을 다룹니다. 조금 어려운 난이도의 코테에서 분할 정복 거듭제곱이 나오는 경우가 있어, 한 번 넣어봤습니다.
>
> n<sup>k</sup> 을 계산할 때, n을 k번 곱하면 k번의 연산이 필요합니다. k가 작다면 시간이 적게 걸리겠지만, 이번 문제처럼 k가 10<sup>12</sup> 같이 매우 큰 수로 주어지는 경우 시간 초과가 발생합니다. 이 때, 분할 정복 거듭제곱을 이용하면 연산을 크게 줄일 수 있습니다. 이번 문제에서는 10<sup>12</sup> 번 연산이 10000번 가량으로 크게 줄어듭니다.
>
> ```python
> # 파이썬 거듭 제곱 내장 모듈 (소요시간 k에 비례)
> def power1(n, k):
>     return n ** k
> 
> # n을 k번 곱하기 (소요시간 k에 비례)
> def power2(n, k):
>     result = 1
>     for _ in range(k):
>         result *= n
>     return result
> 
> # 분할 정복으로 거듭제곱 계산하기 (소요시간 log k에 비례)
> # 한 가지 예시입니다. 재귀 또는 비트 연산으로도 많이 구현합니다.
> def power3(n, k):
>     result = 1
>     # 더 이상 곱할 것이 없을 때까지 진행하자.
>     while k > 0:
>         # 만약 k가 홀수라면, n을 곱하자.
>         if k % 2:
>             result *= n
>         # 다음 과정을 위한 밑작업
>         n *= n
>         k //= 2
>     return result
> ```
>
> 이해에 도움이 될만한 글 링크를 첨부합니다.
>
> https://mygumi.tistory.com/319 , 마이구미의 HelloWorld, 티스토리, 2018.06.06 



- [백준 1937 욕심쟁이 판다](https://www.acmicpc.net/problem/1937)
- [백준 4803 트리](https://www.acmicpc.net/problem/4803)
- [백준 18291 비요뜨의 징검다리 건너기](https://www.acmicpc.net/problem/18291)