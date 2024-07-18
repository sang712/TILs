"""
완전이진트리이므로 주어진 수의 정중앙의 수가 부모노드의 수가 되고
그 수를 기점으로 왼쪽이 왼쪽 노드, 오른쪽이 오른쪽 노드로 재귀방식으로 반복하면 됨
"""
K = int(input())
bi_tree = [[] for _ in range(K)]
cities = list(map(int, input().split()))

def visit(k, cities):
    mid = (2**(K-k)-1)//2
    bi_tree[k].append(cities[mid])
    if mid:
        visit(k+1, cities[:mid])
        visit(k+1, cities[mid+1:])

visit(0, cities)
for level in bi_tree:
    print(*level)