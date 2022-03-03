# def solution(s):
#     num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     for i, j in enumerate(num_list):
#         s = s.replace(j, str(i))
#         print(s)
#     answer = int(s)
#     return answer
#
# def solution(s):
#     num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     for i in range(10):
#         s = s.replace(num_list[i], str(i))
#
#     answer = int(s)
#     return answer
#
# def solution(s):
#     num_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
#     for i, j in num_dict.items():
#         s = s.replace(i, j)
#         print(s)
# 깔끔한 정답들
    answer = int(s)
    return answer

solution('one4seveneight')