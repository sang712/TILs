N = int(input())  
coordinates = [list(map(int, input().split())) for _ in range(N)]

total_distance = 0
for i in range(1, N):
    x1, y1 = coordinates[i-1]
    x2, y2 = coordinates[i]
    total_distance += abs(x1 - x2) + abs(y1 - y2)

print(total_distance)
