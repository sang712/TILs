"""
이중 for문을 이용해 이전의 값들이 현재 값보다 클 때 숫자들의 개수를 세서 저장하도록 하였고
그 중에 가장 큰 값을 출력하였음
"""
N = int(input())
A = list(map(int, input().split()))
dp = [1]
for i in range(1, N):
    a = A[i]
    length = 0
    for j in range(i):
        if A[j] > a:
            length = max(length, dp[j])
    dp.append(1 + length)
print(max(dp))
