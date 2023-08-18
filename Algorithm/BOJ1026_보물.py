"""
가장 큰 수와 가장 작은 수끼리 곱하게 되면
가장 작은 합을 만들 수 있어서 하나는 작은 순, 하나는 큰 순으로 정렬하여
반복문을 돌면서 곱해서 누적 하였음
"""
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
A.sort()
B.sort(reverse=True)
for i in range(N):
    ans += A[i] * B[i]
print(ans)