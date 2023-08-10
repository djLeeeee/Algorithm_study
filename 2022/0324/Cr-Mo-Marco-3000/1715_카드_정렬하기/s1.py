from sys import stdin

def heappush(v):
    global heap
    global heap_count
    heap += [0]
    heap_count += 1
    heap[heap_count] = v

    child = heap_count
    parent = child // 2

    while parent and heap[child] <= heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
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
        if heap[child] > heap[child+1]:
            child = child + 1

    while child <= heap_count and heap[parent] >= heap[child]:
        heap[child], heap[parent] = heap[parent], heap[child]
        parent = child
        child = parent * 2
        if child + 1 <= heap_count:
            if heap[child] > heap[child + 1]:
                child = child + 1
    return return_value

N = int(stdin.readline().rstrip())
heap = [0]
heap_count = 0
# 시간초과 뜰 거 같은데
for tc in range(1, N+1):
    heappush(int(stdin.readline().rstrip()))
cnt = 0
for _ in range(1, N):
    a = heappop()
    b = heappop()
    cnt += a + b
    heappush(a + b)

print(cnt)