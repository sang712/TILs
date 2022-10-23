'''
조건
3≤N≤5,000인 정수
버스 번호는 서로 중복되지 않는다.

풀이
2차원 리스트를 설정해 i와 j가 정해졌을 때, j보다 오른쪽에 조건을 만족하는 
k가 얼마나 있는지 누적합으로 계산하면 되는 문제이다
풀이 설명에서는 리스트(배열)의 첫 항에 i번째의 버스 번호를 사용하여 이해하는 데에 어려움이 있었다
2차원 리스트에 그냥 i번째임을 그대로 사용해도 결과에 큰 차이가 없었다
내가 수정한 풀이 633ms 해설 풀이 613ms

앞으로 3중 for문을 돌려야하는 경우 누적합으로 풀 수 있는지 먼저 생각해 보아야겠다
'''
'''나였다면'''
import sys

N = int(input())
buses = [0] + list(map(int, input().split())) # 편의를 위해 idx와 버스의 번호를 맞추기 위해 [0]을 추가

cnt_k = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    cnt_k[i][N] = 0
    cnt_k[i][N-1] = 1 if buses[i] > buses[N] else 0 # 정렬을 못하는 조건을 만족하면 1 만족하지 않으면 0
    for j in range(N-2, 0, -1): # 오른쪽 부터 더해가는 누적합, j는 최소가 1이니까 1까지만
        if buses[i] > buses[j+1]: # 정렬을 못하는 조건을 만족하면
            cnt_k[i][j] = cnt_k[i][j+1] + 1 # 직전 값 +1
        else: # 아니라면
            cnt_k[i][j] = cnt_k[i][j+1] # 직전 값

ans = 0
for i in range(1, N-1): # j와 k가 있으니 (N+1)-2 범위 까지
    for j in range(i+1, N): # 위와 마찬가지
        if buses[i] < buses[j]:
            ans += cnt_k[i][j]
print(ans)

'''설명대로 구현하기'''
# import sys

# N = int(input())
# buses = [0] + list(map(int, input().split())) # 편의를 위해 idx와 버스의 번호를 맞추기 위해 [0]을 추가

# cnt_k = [[0 for _ in range(N+1)] for _ in range(N+1)]

# for ai in range(1, N+1):
#     cnt_k[ai][N] = 0
#     cnt_k[ai][N-1] = 1 if ai > buses[N] else 0 # 정렬을 못하는 조건을 만족하면 1 만족하지 않으면 0
#     for j in range(N-2, 0, -1): # 오른쪽 부터 더해가는 누적합, j는 최소가 1이니까 1까지만
#         if ai > buses[j+1]: # 정렬을 못하는 조건을 만족하면
#             cnt_k[ai][j] = cnt_k[ai][j+1] + 1 # 직전 값 +1
#         else: # 아니라면
#             cnt_k[ai][j] = cnt_k[ai][j+1] # 직전 값

# ans = 0
# for i in range(1, N-1): # j와 k가 있으니 (N+1)-2 범위 까지
#     for j in range(i+1, N): # 위와 마찬가지
#         if buses[i] < buses[j]:
#             ans += cnt_k[buses[i]][j]
# print(ans)