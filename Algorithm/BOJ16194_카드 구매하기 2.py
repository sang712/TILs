"""
2중 for문과 dp를 이용하여 
특정 개수의 카드를 구매한 금액을 한 묶음으로 쳐서 서로 다른 묶음을 2개 구매했을 때와
그냥 그 카드팩을 구매한 것 중
더 싸게 구매한 것을 저장하는 방식으로 풀이하였음
"""
N = int(input())
P = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(N + 1 - i):
        P[i + j] = min(P[i] + P[j], P[i + j])
print(P[N])