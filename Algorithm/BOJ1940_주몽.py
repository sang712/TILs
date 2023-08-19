"""
탐색하는 방향을 고려하지 않았었는데
덧셈의 결과의 크기에 따라 방향을 정해주었어야 했음
해당 부분을 수정하니 통과되었음
"""
N = int(input())
M = int(input())
ingredient = list(map(int, input().split()))
ingredient.sort()
start, end = 0, N - 1
cnt = 0
while start < end:
    combine = ingredient[start] + ingredient[end]
    if combine == M:
        cnt += 1
        start += 1
        end -= 1
    elif combine < M:
        start += 1
    else:
        end -= 1
print(cnt)
	