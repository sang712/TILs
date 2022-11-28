'''
풀이 방법을 찾아보았더니 대부분 max heap과 min heap을 각각 만들어서
두 곳에서 한 번에 지우는 방식으로 진행하였음
그런데 해당 문제의 테스트케이스가 검증을 잘 못해줘서 맞았다고 나오는 사람들이 있었지만
틀린 사람이 많았음
각 heap에서 최대이든 최소이든을 지우고 다른 heap에서도 지우고 나면
그 다른 heap에서는 heap 구조가 깨지기 때문에 heapify를 적용해야 했음
(* heapify 에서는 list슬라이싱이 적용되지 않으니 인자로 넣기 전에 적용해야함)
차라리 heapify를 적용할 바에는 nlargest로 최댓값 순서로 뽑고 0번 인덱스는 제외하는 방식을 적용하였음
그런데 이렇게 되면 시간초과가 될 것 같았는데 그러지 않아서 조금 이상했음
백준에도 같은 이름의 같은 유형의 문제가 있어서 백준에서도 같은 방법으로 풀어보고
시간 초과가 나는지 확인해야겠음
'''
import heapq

def solution(operations):
    heap = []
    
    for operation in operations:
        command, num = operation.split()
        if command == 'I':
            heapq.heappush(heap, int(num))
        else:
            if not heap:
                continue
            if num == '1':
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
            elif num == '-1':
                heapq.heappop(heap)
        
    answer = [0, 0]        
    if heap:
        answer[1] = heap[0]
        answer[0] = heapq.nlargest(len(heap), heap)[0]
        
    return answer


# solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])