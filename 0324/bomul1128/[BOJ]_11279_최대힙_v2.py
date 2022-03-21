from sys import stdin as s


# max heap 생성
def making_heap(heap, new_num):
    index = len(heap)
    heap.append(new_num)
    while True:
        if heap[index] > heap[index // 2] > 0:
            heap[index], heap[index // 2] = heap[index // 2], heap[index]
            index = index // 2
        else:
            break
    return heap


# max heap 꼭대기 원소 제거
def reorder_heap(heap):
    index = 1
    if len(heap) > 2:
        heap[index] = heap.pop()
    else:
        heap = [0]
    while True:
        try:
            if heap[index * 2] > heap[index] and heap[index * 2] >= heap[index * 2 + 1]:
                heap[index], heap[index * 2] = heap[index * 2], heap[index]
                index = index * 2
            elif heap[index * 2 + 1] > heap[index] and heap[index * 2 + 1] > heap[index * 2]:
                heap[index], heap[index * 2 + 1] = heap[index * 2 + 1], heap[index]
                index = index * 2 + 1
            else:
                break
        except:
            try:
                if heap[index * 2] > heap[index]:
                    heap[index], heap[index * 2] = heap[index * 2], heap[index]
                    index = index * 2
                else:
                    break
            except:
                break
    return heap


# 초기값 설정
N = int(s.readline())
my_heap = [0]

# 문제 해결
for _ in range(N):
    my_input = int(s.readline())
    if my_input == 0:
        if len(my_heap) == 1:
            print(0)
        else:
            print(my_heap[1])
            my_heap = reorder_heap(my_heap)
    else:
        my_heap = making_heap(my_heap, my_input)
