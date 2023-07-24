N = int(input())

bird = 1
time = 0
while N >= 1:
    time += 1
    if N >= bird:
        N -= bird
    else:
        bird = 1
        N -= bird
    bird += 1
print(time)