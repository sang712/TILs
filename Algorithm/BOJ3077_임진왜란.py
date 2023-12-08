N = int(input())
wars = {war: i for i, war in enumerate(input().split())}
hw = input().split()

a = 0
b = N * (N - 1) // 2
for i in range(N):
    for j in range(i + 1, N):
        if wars[hw[i]] < wars[hw[j]]:
            a += 1
print(f'{a}/{b}')