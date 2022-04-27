from itertools import permutations as P

N, K = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
for schedule in P(A, N): # A중에 N개(전부)를 고르는 순열중 에 하나를 골라서
    weight = 500
    for gain in schedule: # 그 순열 순서대로 돌면서 근손실이 나는지 체크
        weight += gain - K
        if weight < 500: # 근손실이 났다면 break
            break
    else:  # break 없이 빠져나왔다면
        answer += 1
print(answer)