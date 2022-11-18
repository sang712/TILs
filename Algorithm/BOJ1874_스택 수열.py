'''
구현 하였음 
<list>.pop()은 시간 복잡도가 O(1)이라서 사실 stack을 구현하는 것에는 deque를 사용할 필요가 없음
deque를 사용한 코드 180ms
deque를 안 쓴 코드 160ms
deque를 안 쓴 코드로 수정하였음
'''
import sys
# from collections import deque
input = sys.stdin.readline

N = int(input())

# stack = deque()
stack = []
result = []
current_number = 0

for i in range(N):
    number = int(input())
    while current_number < number:
        current_number += 1
        stack.append(current_number)
        result.append('+')
        
    if current_number >= number and len(stack):
        pop_number = stack.pop()
        result.append('-')
        if not pop_number == number:
            print("NO")
            break
else:
    print('\n'.join(result))
