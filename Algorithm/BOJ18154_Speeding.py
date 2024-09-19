N = int(input())

# Initialize 2 store times and distances
times = []
distances = []

# Read time and distance 
for _ in range(N):
    t, d = map(int, input().split())
    times.append(t)
    distances.append(d)

max_speed = 0

for i in range(1, N):
    delta_d = distances[i] - distances[i - 1]
    delta_t = times[i] - times[i - 1]
    
    # Calculate speed between the two points
    speed = delta_d / delta_t
    
    # Update max higher
    max_speed = max(max_speed, speed)

print(int(max_speed))
