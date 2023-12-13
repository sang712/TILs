"""
기차가 출발하는 시간을 기준으로 정렬하였고
깜빡 했던 M 값으로 정렬한 기차 시간표를 평행이동? 시킴
그 후에 N을 한 시간동안에 운행하는 기차의 수로 나머지 연산을 해
해당 순서에 맞는 기차를 출력하였음
"""
T, M, N = map(int, input().split())

trains = []
for _ in range(T):
    train, *times = input().split()
    
    for time in times[:-1]:
        trains.append((train, int(time)))
        
trains.sort(key=lambda x: x[1])

for i in range(len(trains)):
    if trains[i][1] >= M:
        trains = trains[i:] + trains[:i]
        break

idx = (N - 1) % len(trains)
print(trains[idx][0])