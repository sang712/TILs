"""
2중 for문으로 돌면서 0부터 첫번째 for문의 인덱스까지의 구간에서
합이 가장 큰 부분 수열을 더하는 방식으로 구현하였음
"""
N = int(input())
sequence = list(map(int, input().split()))
sum_sub = [0] * N
for i in range(N):
    sum_sub[i] = sequence[i]
    for j in range(i):
        if sequence[i] > sequence[j]:
            sum_sub[i] = max(sum_sub[i], sequence[i]+sum_sub[j])
print(max(sum_sub))