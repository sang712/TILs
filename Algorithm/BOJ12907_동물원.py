N = int(input())
animals = list(map(int, input().split()))
level = [0]*N
is_okay = True

for animal in animals:
    if animal >= N:
        is_okay = False
        break
    level[animal] += 1
    if level[animal] > 2:
        is_okay = False
        break

numbers = 1
count = 0
if is_okay:
    for i in range(N):
        if i and level[i-1] < level[i]:
            print(0)
            break
        count += level[i]
        if level[i] == 2:
            numbers *= 2
        if count == N:
            if level[i] == 1:
                numbers *= 2
            print(numbers)
            break
else:
    print(0)