"""
시간 좀 줄여보겠다고 들어온 사람, 나간 사람 체크를 다른 set에 저장했는데
이렇게 되면 한번이라도 나간 사람은 계속 나간 것으로 체크 돼서 틀린 답을 내보내게 되었음
"""
import sys
input = sys.stdin.readline

n = int(input())
people = set()

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        people.add(name)
    elif status == 'leave':
        people.remove(name)

print(*sorted(list(people), reverse=True), sep='\n')