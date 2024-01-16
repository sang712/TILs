import sys
input = sys.stdin.readline

N = int(input())

work_to_do = [list(map(int, input().split())) for _ in range(N)]
work_to_do.sort(key=lambda x: -x[1])

starting_time = 1_000_000
for t, s in work_to_do:
    if t <= s:
        if s <= starting_time:
            starting_time = s - t
        else:
            starting_time -= t
    else:
        print(-1)
        break
else:
    print(starting_time)