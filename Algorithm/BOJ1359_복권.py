"""
구해야 하는 값은
맞는 수가 K개인 경우 * 틀린 수가 M-K인 경우 + 맞는 수가 K+1개인 경우 * 틀린수가 M-K-1인 경우 + ... + 맞는 수가 M개인 경우 * 틀린 수가 0개인 경우
를 N개의 수 중 M개의 수를 뽑는 경우로 나눈 것으로
조합의 확률을 구하는 식을 사용해서 위의 식의 항을 각각 구한 뒤 총합해서 출력하도록 하였음
"""
N, M, K = map(int, input().split())

def comb(a, b):
    result = 1
    for i in range(a, a-b, -1):
        result *= i
    for i in range(b, 0, -1):
        result /= i
    return result

ans = 0
for i in range(K, M + 1):
    ans += comb(M, i) * comb(N - M, M - i) / comb(N, M)
print(ans)