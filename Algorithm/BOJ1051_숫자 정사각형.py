"""
입력을 받아서 3중 for 문을 이용해 정사각형의 변의 길이를 키워가며 비교하며
조건을 모두 부합할 경우에만 길이의 제곱을 입력받아 출력하도록 하였음
"""
N, M = map(int, input().split())
rectangle = [list(map(int, list(input()))) for _ in range(N)]

cnt = 1
for i in range(N):
    for j in range(M - 1):
        num = rectangle[i][j]
        for k in range(j + 1, M):
            if rectangle[i][k] == num:
                l = k - j
                if i + l < N and rectangle[i + l][j] == num and rectangle[i + l][k] == num:
                    cnt = max(cnt, (l + 1) ** 2)
print(cnt)