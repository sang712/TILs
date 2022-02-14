N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

K = int(input())

for _ in range(K):
    sumation = 0
    i, j, x, y = map(int, input().split())
    for r in range(i-1, x):
        # for문 한 depth 깊게 하는 것 보다 sum을 쓰니 시간 초과가 안 뜨는 구간이 길어짐
        # pypy3를 사용하니 시간 초과가 아예 안 뜨고 통과함
        sumation += sum(arr[r][j-1:y])
    print(sumation)