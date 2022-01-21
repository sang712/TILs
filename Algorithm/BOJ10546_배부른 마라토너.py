import sys
N = int(input())

marathoners = {}
for _ in range(N):
    name = sys.stdin.readline()
    if name in marathoners:
        marathoners[name] += 1
    else:
        marathoners[name] = 0


for _ in range(N-1):
    name = sys.stdin.readline()
    if marathoners[name]:
        marathoners[name] -= 1
    else:
        marathoners.pop(name)

print(marathoners.popitem()[0]) # popitem()하면 마지막 키, 값을 가져오고 0번 인덱스를 찍으면 키값을 가져옴