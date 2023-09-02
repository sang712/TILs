import sys
input = sys.stdin.readline

N = int(input())
time = []
for _ in range(N):
    A, B = map(int, input().split())
    time.append(A - B)

time.sort()

print(time[N // 2] - time[(N - 1) // 2] + 1)
