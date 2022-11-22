'''
1. 자식 노드끼리의 절댓값이 같을 때
2. 부모와 자식 노드의 절댓값이 같을 때

스파게티 코드가 되었지만 직접 구현했다는 것에 만족하고
heapq 라이브러리를 이용해서 푸는 방법도 모색할 것
'''
import sys
input = sys.stdin.readline

N = int(input())

heap = []

def heapq_push(number):
    heap.append(number)
    length = len(heap)
    child = length-1
    while True:
        if not child:
            break
        parent = (child-1)//2
        if abs(heap[parent]) > abs(heap[child]):
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
        elif abs(heap[parent]) == abs(heap[child]):
            heap[parent], heap[child] = min(heap[parent], heap[child]), max(heap[parent], heap[child])
            child = parent
        else:
            break

def heapq_pop():
    if not heap:
        return 0
    parent = 0
    minimum = heap[parent]
    length = len(heap)
    heap[parent] = heap[length-1]
    heap.pop()
    length -= 1
    while True:
        child1 = (parent*2) + 1
        child2 = (parent*2) + 2
        if child1 < length:
            if child2 < length:
                if abs(heap[child1]) < abs(heap[child2]):
                    if abs(heap[parent]) > abs(heap[child1]):
                        heap[parent], heap[child1] = heap[child1], heap[parent]
                        parent = child1
                    elif abs(heap[parent]) == abs(heap[child1]):
                        if heap[parent] > heap[child1]:
                            heap[parent], heap[child1] = heap[child1], heap[parent]
                            parent = child1
                        else:
                            break
                    else:
                        break
                    continue
                elif abs(heap[child1]) > abs(heap[child2]):
                    if abs(heap[parent]) > abs(heap[child2]):
                        heap[parent], heap[child2] = heap[child2], heap[parent]
                        parent = child2
                    elif abs(heap[parent]) == abs(heap[child2]):
                        if heap[parent] > heap[child2]:
                            heap[parent], heap[child2] = heap[child2], heap[parent]
                            parent = child2
                        else:
                            break
                    else:
                        break
                    continue
                elif abs(heap[child1]) == abs(heap[child2]):
                    if abs(heap[parent]) > abs(heap[child1]):
                        if heap[child1] <= heap[child2]:
                            heap[parent], heap[child1] = heap[child1], heap[parent]
                            parent = child1
                        else:
                            heap[parent], heap[child2] = heap[child2], heap[parent]
                            parent = child2
                        continue
                    if abs(heap[parent]) == abs(heap[child1]):
                        if heap[parent] > heap[child1]:
                            heap[parent], heap[child1] = heap[child1], heap[parent]
                            parent = child1
                        elif heap[parent] > heap[child2]:
                            heap[parent], heap[child2] = heap[child2], heap[parent]
                            parent = child2
                        else:
                            break
                        continue
            elif abs(heap[parent]) >= abs(heap[child1]):
                heap[parent], heap[child1] = heap[child1], heap[parent]
                parent = child1
                continue
            elif abs(heap[parent]) == abs(heap[child1]) and heap[parent] >= heap[child1]:
                heap[parent], heap[child1] = heap[child1], heap[parent]
                parent = child1
                continue
        break
    return minimum
        
output = []

for _ in range(N):
    x = int(input())
    
    if x:
        heapq_push(x)
    else:
        output.append(str(heapq_pop()))
    print(heap)

print('\n'.join(output))