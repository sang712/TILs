from itertools import permutations

N, M = map(int, input().split())

satisfaction = []
for i in range(N):
    satisfaction.append(list(map(int, input().split())))

num_list = [m for m in range(M)]

max_num = 0
for perm in permutations(num_list, 3):
    perm0, perm1, perm2 = perm
    sumation = 0
    for i in range(N):
        sumation += max(satisfaction[i][perm0], satisfaction[i][perm1], satisfaction[i][perm2])
    if sumation > max_num:
        max_num = sumation

print(max_num)