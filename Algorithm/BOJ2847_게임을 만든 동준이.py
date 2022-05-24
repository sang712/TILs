N = int(input())
stages = [0] * 100
count = 0
for i in range(N):
    this = i
    stages[this] = int(input())
    if i == 0:
        continue
    while this > 0:
        while stages[this] <= stages[this-1]:
            stages[this-1] -= 1
            count += 1
        this -= 1

print(count)
