"""
문제에서 요구한 사항을 그대로 deque로 구현하여 풀이하였음
"""
from collections import deque
N = int(input())
cards = deque(range(1, N + 1))

while len(cards) > 1:
    print(cards.popleft())
    cards.append(cards.popleft())
print(cards.pop())