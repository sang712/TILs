"""
변환 방식을 문제가 요구하는대로 구현한 뒤
BFS 방식으로 변환횟수를 카운팅하며 답을 찾도록 하였음

200ms가 걸렸는데 더 빨리 하려면 list-tuple 변환을 하지 않고 tuple로만 사용하는 것일 것임
그러기 위해서는 list변환을 사용하지 않고 하드 코딩으로 새로운 tuple을 만들어내는 방식을 사용하면 될 것임
"""

import collections
magic_square = tuple(map(int, input().split()))
commands = ['A', 'B', 'C', 'D']

def transform(magic_square, command):
    result = list(magic_square)
    if command == 'A':
        for i in range(4):
            result[i], result[7-i] = result[7-i], result[i]
    elif command == 'B':
        result = [result[3]] + result[:3] + result[5:8] + [result[4]]
    elif command == 'C':
        result[1], result[2], result[5], result[6] = result[2], result[5], result[6], result[1]
    elif command == 'D':
        result[0], result[4] = result[4], result[0]
    return tuple(result)

q = collections.deque([((1, 2, 3, 4, 5, 6, 7, 8), 0)])
counter = {}
while q:
    current_square, l = q.popleft()
    if current_square == magic_square:
        ans = l
        break
        
    for command in commands:
        result = transform(current_square, command)
        
        if result in counter:
            continue
        counter.setdefault(result, 1)
        
        q.append((result, l+1))
print(ans)