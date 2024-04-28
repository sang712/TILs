"""
머리로 풀이 방법을 구상해 보았을 땐 복잡해보이고 4중 for 문을 사용할 거라 생각했는데
막상 구현해 보니 왜 실버5 문제인지 알겠는 문제
"""
N, M = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(M)]

matrix3 = [[0]*K for _ in range(N)]
for i in range(N):
    for j in range(K):
        element = 0
        for m in range(M):
            element += matrix1[i][m] * matrix2[m][j]
        matrix3[i][j] = element
for row in matrix3:
    print(*row)