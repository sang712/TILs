'''
knapsack algorithm을 검색하여 공부하고 구현하였음

knapsack algorithm은 가치와 무게를 가지는 물건들을 제한된 무게 안에서 가치를 최대화하는 유형의 문제임
knapsack algorithm에도 여러 유형이 있는데 
이 문제는 물건의 일부를 챙길 수 있는 경우가 아닌 챙기거나 말거나의 경우인 0-1 knapsack algorithm임

이 때, dp로 문제를 해결할 수 있는데, 물건의 종류의 수 +1 * 제한된 무게 +1 차원의 리스트를 만들고
물건들의 수 만큼 for문을 돌면서 
제한 무게를 1씩 증가시키며(제한된 무게 만큼 for문을 돌면서) 물건을 챙길지 말지 결정함
- 현재 물건의 무게가 제한 조건보다 크다면, 해당 물건을 챙기지 못 하므로 무시하고, 
  직전 물건을 같은 제한 무게로 비교해본 결과를 바로 가져옴
- 현재 물건의 무게가 제한 조건보다 작다면, 해당 물건을 챙길 수 있으므로, 다음 중 큰 값을 고름
  - 물건을 챙길 경우, 
    직전 물건을 현재 제한 무게에서 현재 물건의 무게를 뺀 제한 무게와 비교한 결과와 현재 물건의 무게의 합
  - 물건을 챙기지 않을 경우,
    직전 물건을 같은 제한 무게로 비교해본 결과
문제에서 요구하는 답은 dp의 마지막 행, 마지막 열에 할당되게 됨

공부한 대로 구현한 뒤에 knapsack 알고리즘은 자체적으로 최적화가 필요하다고 작성된 것을 발견하여
최적화할 수 있는 방안이 없나 생각하다가 dp를 초기에 전부 만들지 않고 append()함수를 이용하면 
속도를 개선할 수 있으리라 판단하여 개선함
6188ms -> 5720ms으로 개선하였음
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 처음 구현한 코드
'''
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(N):
    W, V = map(int, input().split())
    for j in range(K):
        if W > j + 1:
            knapsack[i + 1][j + 1] = knapsack[i][j + 1]
        else:
            knapsack[i + 1][j + 1] = max(knapsack[i][j + 1], knapsack[i][j + 1 - W] + V)
print(knapsack[N][K])
'''

# 시간을 개선한 코드
knapsack = [[0 for _ in range(K + 1)]]

for i in range(N):
    W, V = map(int, input().split())
    sack_row = [0]
    for j in range(K):
        if W > j + 1:
            sack_row.append(knapsack[i][j + 1])
        else:
            sack_row.append(max(knapsack[i][j + 1], knapsack[i][j + 1 - W] + V))
    knapsack.append(sack_row)

print(knapsack[N][K])