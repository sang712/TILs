"""
링크드리스트 문제라고 해서 이렇게 풀었는데
스택을 2개 두고 한 개의 스택에 모든 값을 몰아넣은 뒤, 커서의 오른쪽으로 넘어가는 값은
다른 스택에 넣어버리는 방식으로 구현하면 더 빠른 풀이가 가능함
단 이 때 스택 자료 구조이므로 두 번째 스택에는 값이 역순으로 담겨있음

연결리스트 1152ms 스택, 프린트 리스트 388ms, 스택, 프린트 조인 248ms

+) print(*리스트, sep='')보다
print(''.join())이 더 빠른 연산속도를 자랑함
"""
# import sys
# class LinkedList():
#     def __init__(self, value: str) -> None:
#         self.value = value
#         self.parent = None
#         self.child = None

# text = input()
# prev_node = None
# for s in text:
#     node = LinkedList(s)
#     if prev_node:
#         prev_node.child = node
#     node.parent = prev_node
#     prev_node = node

# M = int(input())
# cursor = LinkedList('')
# if prev_node:
#     prev_node.child = cursor
# cursor.parent = prev_node

# for _ in range(M):
#     command, *char = sys.stdin.readline().split()
#     if command == 'L':
#         if cursor.parent: cursor = cursor.parent
#     elif command == 'D':
#         if cursor.child: cursor = cursor.child
#     elif command == 'B':
#         if cursor.parent:
#             if cursor.parent.parent:
#                 grandparent = cursor.parent.parent
#                 grandparent.child, cursor.parent = cursor, grandparent
#             else:
#                 cursor.parent = None
#     elif command == 'P':
#         node = LinkedList(char[0])
#         if cursor.parent:
#             cursor.parent.child, node.parent = node, cursor.parent
#         node.child, cursor.parent = cursor, node
            
# while cursor.parent:
#     cursor = cursor.parent
# ans = []
# while cursor:
#     ans.append(cursor.value)
#     cursor = cursor.child
# print(*ans, sep='')

import sys
left = list(input())
right = []
M = int(input())
for _ in range(M):
    command = sys.stdin.readline().strip()
    if command == 'L':
        if left: right.append(left.pop())
    elif command == 'D':
        if right: left.append(right.pop())
    elif command == 'B':
        if left: left.pop()
    elif command[0] == 'P':
        left.append(command[2])
while right:
    left.append(right.pop())
print(*left, sep='')
