"""
음수 간선이 존재하기 때문에 벨만-포드 알고리즘을 사용함

벨만-포드의 알고리즘의 특징은 다음과 같음
시작 정점으로부터 모든 정점까지의 거리를 알 수 있음
간선이 음수여도 적용할 수 있다. 단, 음수 간선이 포함된 사이클이 있을 경우 결과를 얻지는 못 함
한 번 처리할 때 모든 간선을 확인하므로 시간 복잡도는 O(VE)
정점의 개수만큼 처리를 하였을 때는 무한 반복되는 사이클이 존재한다는 뜻임 즉 음수 간선이 포함된 사이클이 존재하는지 확인할 수 있음

[문제의 이슈를 정리한 글](https://www.acmicpc.net/board/view/72995)

문제의 이슈를 확인하면 시작점이 따로 없기 때문에 시작점을 정해놓고 풀면 틀린 답을 얻게 된다는 점과
파이썬의 float('inf')를 사용하게 되면 INF + 음수 연산의 결과가 INF로 그대로 나오기 때문에 틀린 답을 얻게 된다는 점을 확인하였음

위의 두가지를 고려하여 벨만 포드 알고리즘을 다시 구현하였고 약 2800ms가 소요되었음

그 후에 더 빠른 코드를 찾아보니 중간에 탈출할 수 있도록 플래그를 설정하는 코드가 있었음
해당 코드를 참고하여 값의 갱신이 더이상 일어나지 않으면 탈출하도록 구현하였더니 참고한 코드보다 2배 빠른 결과를 얻게 되었음
344ms 소요되었음
"""
import sys
input = sys.stdin.readline

# 음수 간선이 있고 inf체크를 안 하는 경우에는 inf + 음수 = inf이기 때문에 유한수로 정해야 함
# 사실 시작점이 없기 때문에 0으로 해도 무방함
INF = 10001

def bellman_ford(N, edges):
    dists = [INF for _ in range(N + 1)]
    for _ in range(N - 1):
        # 모든 정점이 연결이 되어있지 않을 경우를 확인하기 위한 플래그
        updated = False
        for cur_node, next_node, cost in edges:
            # 원래 시작점을 체크하기 위해 출발점이 INF인 경우를 제외하는데
            # 이 문제의 경우 시작점이 따로 없고 음수 간선이 포함된 사이클이 존재하는지 판단만 하면 되므로 
            # dists[cur_node] != INF # 을 검사하는 부분을 지우도록 함
            if dists[next_node] > dists[cur_node] + cost:
                dists[next_node] = dists[cur_node] + cost
                updated = True
                
        if not updated: # 정점이 연결되어 있지 않아서 도중에 끝난다면 탈출하기
            return False
    
    for cur_node, next_node, cost in edges:
        if dists[next_node] > dists[cur_node] + cost:
            return True
        
    return False


for tc in range(int(input())):
    N, M, W = map(int, input().split())
    
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    print('YES' if bellman_ford(N, edges) else 'NO')