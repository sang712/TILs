'''
오기가 생겨서 직접 힙큐를 구현해보기로 하였고 그 결과 여러 시행착오가 있었음
1. pop을 할 때 자식 노드에서 우선순위가 높은 것과 비교해야 하는데 이 것과 관계 없이
왼쪽거를 비교해보고 오른쪽 거를 비교해보는 순서로 비교하는 로직을 짰기 때문에 틀렸음
(자식 노드 간의 우선은 정해지지 않았음에 유의해야 함)
2. 수정을 하고나니 조건문이 너무 많아졌는데 while을 탈출하는 문구를 빠뜨려 시간초과가 남
조건문을 합쳐서 몇 줄을 줄이고 else break(6줄) 대신에 continue와 break(4줄)을 이용해 
continue를 타지 않으면 그냥 알아서 탈출이 되도록 하였음

덕분에 힙큐에 대한 이해를 하게 되었고 다음에는 import heapq를 이용하여 풀어야겠다고 생각함

+) 힙큐 동작 과정
# 푸시
1. 맨 마지막 항에 해당 숫자를 추가한다
2. 부모 노드와 비교해서 우선순위가 높으면 부모와 자리를 바꾼다
3. 루트 노드에 닿거나 교환이 멈추면 그만둔다

# 팝
1. 루트 노드를 팝한다
(구현할 때에는 pop(1)의 시간복잡도가 O(N)이기 때문에 값만 복사하였음)
2. 가장 마지막에 있는 노드의 값을 루트 노드에 넣는다
(구현할 때에는 부모에서 pop을 안 했기 때문에 pop()해서 넣어 주었음)
3. 루트 노드에서 자식노드와 비교해서 우선순위가 낮으면 밑으로 내린다
(이 때 우선 순위가 더 높은 자식노드와만 비교한다)
4. 끝 노드에 닿거나 교환이 멈추면 그만둔다

# 공통 사항
리스트를 사용하였기 때문에 idx에러가 날 수 있어 해당 부분을 고려해야 한다
특히 pop의 경우 자식 노드 2개 있는지 1개 있는지 확인 해서 로직을 짜야하는 점이 불편했다
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
        if heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent
        else:
            break

def heapq_pop():
    if not heap:
        return 0
    parent = 0
    maximum = heap[parent]
    length = len(heap)
    heap[parent] = heap[length-1]
    heap.pop()
    length -= 1
    while True:
        child1 = (parent*2) + 1
        child2 = (parent*2) + 2
        if child1 < length:
            if child2 < length:
                if heap[child1] >= heap[child2] and heap[parent] < heap[child1]:
                    heap[parent], heap[child1] = heap[child1], heap[parent]
                    parent = child1
                    continue
                elif heap[child1] < heap[child2] and heap[parent] < heap[child2]:
                    heap[parent], heap[child2] = heap[child2], heap[parent]
                    parent = child2
                    continue
            elif heap[parent] < heap[child1]:
                heap[parent], heap[child1] = heap[child1], heap[parent]
                parent = child1
                continue
        break
    return maximum
        
output = []

for _ in range(N):
    x = int(input())
    
    if x:
        heapq_push(x)
    else:
        output.append(str(heapq_pop()))

print('\n'.join(output))