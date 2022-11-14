'''
파이썬의 pop()이 순차적으로 따라가서 마지막 항목을 pop하기 때문에 시간 복잡도가 높아질 거라 생각했는데
전혀 그런 것이 아니고 똑같이 O(1)만 됨
pop(0)가 시간복잡도가 O(N)임, 맨 앞에 것을 빼고 순차적으로 앞으로 땡기기 때문
cnt를 넣어 풀면 132ms, cnt를 삭제하고 풀면 124ms가 걸림
sumation 변수에 더했다 뺐다를 하기 때문에 마지막에 그냥 sum 함수를 사용하는 것으로 바꾸면? 116ms가 걸림
'''
import sys

K = int(input())

numbers = []
sumation = 0
cnt = -1

for _ in range(K):
    integer = int(sys.stdin.readline())
    if integer:
        numbers.append(integer)
        sumation += integer
        cnt += 1
    else:
        sumation -= numbers.pop(cnt)
        cnt -= 1
print(sumation)

''' 104ms 인 답안
import sys
input()
input = sys.stdin
m = []
for i in map(int, input):
    m.append(i) if i != 0 else m.pop()
print(sum(m))
'''