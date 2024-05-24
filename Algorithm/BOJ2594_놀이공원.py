"""
시간의 덧셈 뺄셈을 용이하게 하기 위해 시간에 60을 곱해 사용했고
기본 시간인 10시를 600
22시를 1320으로 나타내었음
그 후에 마지막으로 일한 시간을 갱신하면서
쉬는 시간을 계산해 비교하여 최대 쉬는 시간으로 갱신하는 방법을 이용하였음
"""
import sys
input = sys.stdin.readline

ride = [[600, 600], [1320, 1320]]
for _ in range(int(input())):
    x, y = input().split()
    x = int(x[:2]) * 60 + int(x[2:]) - 10
    y = int(y[:2]) * 60 + int(y[2:]) + 10
    ride.append([x, y])
ride.sort()

rest = 0
last = 600

for run, stop in ride:
    rest = max(rest, run - last)
    last = max(last, stop)

print(rest)