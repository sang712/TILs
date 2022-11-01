chess = list(map(int, input().split()))
chess[0] -= 1
chess[1] -= 1
chess[2] -= 2
chess[3] -= 2
chess[4] -= 2
chess[5] -= 8
for i in range(len(chess)):
    chess[i] *= -1

print(*chess)