"""
인오더가 중위순회, 포스트오더가 후위순회인 것을 알고 재복습하여 문제를 풀이 하였음
그리하여 포스트오더로 루트의 노드 번호를 찾고, 
루트의 노드 번호와 인오더를 이용하여 루트의 인덱스를 구하고
이를 통해 왼쪽 트리와 오른쪽 트리의 길이를 구하였음
이렇게 구한 길이로 왼쪽 트리와 오른쪽 트리의 경우로 나누어서 
재귀 함수를 통해 분할정복을 하도록 하였음

처음에는 함수에 슬라이싱된 트리를 넘겨주었는데 
이것은 시간초과의 원인이 되어 슬라이싱을 하지 않고 인덱스를 넘겨주는 방향으로 다시 구현하였음
그런데 간과했던 다른 문제점은 인오더의 루트의 인덱스를 구하는 과정에서
재귀함수 특성상 너무 많은 시간을 소모하게 되었음
그래서 처음에 for문을 통해서 인오더의 숫자 별 인덱스 값을 별도로 저장해두고
나중에 인덱스를 찾을 때 사용하였음
"""
import sys
sys.setrecursionlimit(10**6)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
in_order_location = [0 for _ in range(n+1)]
for i in range(n):
    in_order_location[in_order[i]] = i
pre_order = []

# def rebuild_pre(in_order, post_order):
#     if not post_order:
#         return
#     root = post_order.pop()
#     pre_order.append(root)
    
#     root_idx = in_order.index(root)
#     rebuild_pre(in_order[:root_idx], post_order[:root_idx])
#     rebuild_pre(in_order[root_idx+1:], post_order[root_idx:])

def rebuild_pre(in_order_idx, post_order_idx, length):
    if not length:
        return
    root = post_order[post_order_idx+length-1]
    pre_order.append(root)
    
    # in_order_root_idx = in_order_idx + in_order[in_order_idx:in_order_idx+length].index(root)
    in_order_root_idx = in_order_location[root]
    left_length = in_order_root_idx - in_order_idx
    right_length = length - left_length - 1
    
    rebuild_pre(in_order_root_idx-left_length, post_order_idx, left_length)
    rebuild_pre(in_order_root_idx+1, post_order_idx+left_length, right_length)
    

# rebuild_pre(in_order, post_order)
rebuild_pre(0, 0, n)
print(*pre_order)