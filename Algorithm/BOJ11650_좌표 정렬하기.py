'''
input의 개수가 최대 10만개 이므로 sys.stdin.readline을 사용하였음
python에서 제공하는 O(nlogn)를 이용하여 풀었음
'''
import sys
input = sys.stdin.readline
N = int(input())

positions = []
for _ in range(N):
    positions.append(list(map(int, input().split())))
    
positions.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    x, y = positions[i]
    print(f'{x} {y}')