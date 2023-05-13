"""
문제를 보고 유추하여 별을 찍어 제출
별로 만든 박스로 이전까지 만든 별을 감싸 출력하는 것이었음
반복문을 돌면서 해당 반복까지 만들어진 별상자는 좌우에 공백과 별 하나씩으로 감쌌고
위아래에 별로만 된 부분과 별과 공백으로 이루어진 부분을 넣어 다음단계로 넘어가도록 하였음
위 아래에 추가하는 것에 편의를 위해 deque를 이용하였음
"""
from collections import deque

N = int(input())

ans = deque('*')

for i in range(1, N):
    for _ in range(len(ans)):
        ans.append('* ' + ans.popleft() + ' *')
    ans.appendleft('*' + ' ' * (i * 4 - 1) + '*')
    ans.appendleft('*' * (i * 4 + 1))
    ans.append('*' + ' ' * (i * 4 - 1) + '*')
    ans.append('*' * (i * 4 + 1))
    
print(*ans, sep='\n')