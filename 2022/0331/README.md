# 3월 31일 알고리즘 스터디

지금까지 배웠던 알고리즘과 자료 구조 활용하기

> deque 라이브러리 사용하기
>
> ```python
> from collections import deque
> 
> my_arr = deque() 		# my_arr를 덱 구조 선언
> my_arr.append(x) 		# my_arr의 오른쪽 끝에 x를 삽입
> my_arr.appendleft(y) 	# my_arr의 왼쪽 끝에 x를 삽입
> z = my_arr.pop() 		# my_arr의 오른쪽 끝에서 원소를 뽑아 z에 저장
> w = my_arr.popleft() 	# my_arr의 왼 끝에서 원소를 뽑아 z에 저장
> ```

> heapq 라이브러리 사용 방법
>
> ```python
> import heapq
> 
> heapq.heapify(my_list) 			# my_list를 힙 구조로 변경
> heapq.heappush(my_list, my_num)	# 힙 my_list에 원소 my_num 추가
> x = heapq.heappop(my_list) 		# 힙 my_list에서 최솟값을 뽑아 x에 저장
> ```



- [백준 5430 AC](https://www.acmicpc.net/problem/5430)
- [프로그래머스 수식 최대화](https://programmers.co.kr/learn/courses/30/lessons/67257)  *카카오 기출
- [백준 5619 세 번째](https://www.acmicpc.net/problem/5619)
- [백준 14502 연구소](https://www.acmicpc.net/problem/14502)  *삼성 SW 역량 테스트 기출
