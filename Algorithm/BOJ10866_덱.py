'''
문제에서 요구하는 대로 구현하였음
10835 큐 문제와 마찬가지로 strip()을 사용하였음
'''
import sys
input = sys.stdin.readline
N = int(input())

dq = []
length = -1
for _ in range(N):
  command = input().strip()
  if command == 'pop_front':
    if length >= 0:
      print(dq.pop(0))
      length -= 1
    else:
      print(-1)
  elif command == 'pop_back':
    if length >= 0:
      print(dq.pop(length))
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
      print(dq[0])
    else:
      print(-1)
  elif command == 'back':
    if length >= 0:
      print(dq[length])
    else:
      print(-1)
  elif command.startswith('push_front'):
    command, num = command.split()
    dq = [int(num)] + dq
    length += 1
  elif command.startswith('push_back'):
    command, num = command.split()
    dq.append(int(num))
    length += 1
