"""
인덱스 하나하나를 돌면서 해당 위치부터 마지막까지 소트를 하여 
가장 큰 수를 맨 앞으로 가져오는 방식으로 정렬하고
S가 작다면 소트할 때 해당 위치부터 +S까지만 소트하여 한 칸 씩 앞으로 가져오는 방법으로 풀이하였음

처음에는 그냥 무턱대고 오른쪽이 크면 교환하고 그랬는데 이렇게 하면 정렬이 잘 안 되고
그 다음에는 인덱스 하나하나 돌면서 그 수가 제자리를 찾을 때까지 
계속 왼쪽 혹은 계속 오른쪽으로 이동하도록 구현하였는데
대신 이렇게 하면 사전순으로 마지막이 되도록 하라는 조건을 만족하지 못 함

아무튼 사용했던 반례
입력
10
1 2 3 4 5 6 7 8 9 10
17
출력
10 9 1 2 3 4 5 6 7 8

"""
N = int(input())
A = list(map(int, input().split()))
S = int(input())

idx = 0
for i in range(N):
    if S <= 0:
        break
    idx = A.index(sorted(A[i:i + S + 1], reverse=True)[0])
    while idx > 0 and S > 0:
        if A[idx - 1] < A[idx]:
            A[idx - 1], A[idx] = A[idx], A[idx - 1]
            idx -= 1
            S -= 1
            continue
        break
print(*A)