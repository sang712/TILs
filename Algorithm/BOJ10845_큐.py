'''
입력이 많아서 sys.stdin.readline을 사용하였고 요구사항대로 구현하였음
input값에 \n이 포함되어있어 strip()을 사용하여 해당 부분을 제거하였음
'''
import sys
input = sys.stdin.readline
N = int(input())

q = []
length = -1
for _ in range(N):
  command = input().strip()
  if command == 'pop':
    if length >= 0:
      print(q.pop(0))
      length -= 1
    else:
      print(-1)
  elif command == 'size':
    print(length+1)
  elif command == 'empty':
    if length == -1:
      print(1)
    else:
      print(0)
  elif command == 'front':
    if length >= 0:
      print(q[0])
    else:
      print(-1)
  elif command == 'back':
    if length >= 0:
      print(q[length])
    else:
      print(-1)
  elif command.startswith('push'):
    command, num = command.split()
    q.append(int(num))
    length += 1
