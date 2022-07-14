# 0721 알고리즘 스터디

> 로봇 프로젝트 같은 문제의 경우, 테스트 케이스가 총 몇 개인지 알려주지 않고 입력의 끝까지 출력을 해야 하는 문제 입니다. 이런 경우, 몇 가지 해결법이 있습니다.
>
> 1. **try - except 예외문 활용 (추천)**
>
>    에러가 발생하면 입력을 중지하는 방법입니다.
>
>    - `ValueError` : 부적절한 자료형을 함수 인자로 넘긴 경우입니다. 이 문제에서는, 공백에 `int` 함수를 적용하려는 경우 발생합니다. 
>    - `EOFError` : 'End of file'의 줄임말로, 더 이상 입력받을 것이 없으나 `input` 함수를 실행한 경우에 발생하는 에러입니다.
>
>    ```python
>    while True:
>        try:
>            x = int(input())
>        except ValueError or EOFError:
>            break
>        ... # 이 후 코드 작성
>    ```
>
> 2. **`sys.stdin.read()`, `next()`와 예외문 사용 (비추)**
>
>    입력 파일을 모두 읽어오고, `next`라는 함수로 map 객체에서 다음 데이터를 읽어오다가 map 객체가 끝이 나면 (`StopIteration`) 그대로 함수를 종료하는 방식입니다.
>
>    실행 속도 면에서 이 쪽이 대부분의 경우에 더 빨라 종종 사용하는 방법이긴 한데, 솔직히 추천드리지 않습니다. 굳이 실행 속도가 걱정이라면 다른 언어로 하는 게 맞습니다.
>
>    ```python
>    import sys
>    
>    input = map(int, sys.stdin.read().split())
>    while True:
>        try:
>            x = next(input)
>        except StopIteration:
>            break
>        ... # 이 후 코드 작성. 이 때 input 함수 대신 next(input)으로 써야 함.
>    ```
>
> 국내에서 출제된 문제에서는 이렇게 테스트 케이스가 정확히 명시되지 않는 경우가 매우 드무니, Python 작동 원리를 공부하시는 게 아니라면 "아~, 이런 방법도 있구나" 하고 넘어가셔도 괜찮을 것 같습니다! 이런 스타일은 유럽에서 출제되는 문제 스타일입니다.

- [백준 3649 로봇 프로젝트](https://www.acmicpc.net/problem/3649)
- [백준 9935 문자열 폭발](https://www.acmicpc.net/problem/1774)
- [백준 1774 우주신과의 교감](https://www.acmicpc.net/problem/1774)
