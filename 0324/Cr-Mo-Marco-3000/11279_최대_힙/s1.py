from sys import stdin


def heappush(v):
    global heap_count
    global heap
    heap_count += 1
    if heap_count == len(heap):
        heap += [0]
    heap[heap_count] = v

    child = heap_count
    parent = heap_count // 2

    while parent and heap[parent] < heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


def heappop():
    global heap_count
    return_value = heap[1]
    heap[1] = heap[heap_count]
    heap_count -= 1

    parent = 1
    child = parent * 2
    if child + 1 <= heap_count:
        if heap[child] < heap[child + 1]:
            child = child + 1

    while child <= heap_count and heap[parent] < heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heap_count:
            if heap[child] < heap[child + 1]:
                child = child + 1

    return return_value

T = int(stdin.readline().rstrip())
heap_count = 0
heap = [0]

for tc in range(1, T+1):
    order = int(stdin.readline().rstrip())
    # print(heap_count)
    if order == 0:
        if not heap_count:
            print(0)
        else:
            print(heappop())
    else:
        heappush(order)
