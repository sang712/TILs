'''
dp로 푸는데 정방향으로 루프를 돌려서 시간 낭비를 하였음
루프를 뒤로 돌려서 마지막 날부터 처리를 하였음
해당 날짜부터 처리가 가능하다면 
마지막 날부터 다음날까지의 벌 수 있는 금액과
일처리를 끝내고 받는 금액 + 마지막 날부터 일처리가 끝난 날의 다음날까지의 금액을 비교하여 큰 값을 넣고
해당 날짜의 일을 처리하지 못하면 그냥 다음 날까지 벌 수 있는 금액을 넣었음 
개선) dp 길이 N으로 해서 사용할 때는 i+T 때문에 i가 최대일 때를 예외처리 했어야 했는데
N+1로 하고 나서는 해당 부분을 고려하지 않아도 되었음
개선2) max(*dp)로 출력하니 N이 1일 때 dp가 리스트가 되지 않아서 type error가 났는데 해당 문제도 N+1로 해결됨
대신 시간은 max(*dp)나 dp[0]이나 마찬가지였음
시도) N+1이 되면서 "if i < N-1 else P" 부분도 고려할 필요가 없어져서 지웠는데 4ms가 늘었음
'''
N = int(input())
dp = [0] * (N+1)
works = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-1, -1, -1):
    T, P = works[i]
    # print(i, T, i+T-1)
    if i + T-1 < N:
        dp[i] = max((dp[i+T] + P), dp[i+1]) if i < N-1 else P
        # print(f'{i}번째 는{dp[i]}')
    else:
        dp[i] = dp[i+1] if i < N-1 else dp[i]
# print(max(*dp))
print(dp[0])
