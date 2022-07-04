import sys
input = sys.stdin.readline

N = int(input())

triangle = [0 for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(len(line)-1, -1, -1):
        if j == 0:
            triangle[j] += line[j]
        elif 0 < j < len(line)-1:
            triangle[j] = max(triangle[j-1], triangle[j]) + line[j]
        else:
            triangle[j] = triangle[j-1] + line[j]
print(max(triangle))