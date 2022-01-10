# 미완성
# N = int(input())
#
# def combi(x, y):
#     a = (x-1)+y # 1의 자리는 5로 고정이므로 고려해야할 5의 개수 1개 빼기
#     output = 1
#     for i in range(a, max(x-1,y), -1):
#         output *= i
#     for i in range(1, min(x-1,y)+1):
#         output /= i
#     return output
#
# def countcase(num5, num1):
#     # 1의 자리는 5 고정, 전체가 3의 배수이면 됨
#     # 5나 1이 3의 배수개이면 3의 배수이고, 3으로 나눈 나머지가 같을 때도 3의 배수이면 됨
#     if (num5 % 3 == num1 % 3):
#         return combi(num5, num1)
#     else:
#         return 0
#
# case = 0
# if N > 1: # 1자리는 15 미만이므로 규칙에서 예외이므로 두자리수부터 판단
#     # N에 5의 개수를 1개씩 늘려서 경우의 수 판단
#     for i in range(1, N+1): # 5는 무조건 1개 이상이어야 함
#         case += countcase(i, N-i) # N에 5가 i개, 1이 N-i개일 때의 가능한 경우의 수
#     print(case%1000000007)
# else:
#     print(0)

N = int(input())

dp = [[0,0,0] for i in range(1516)]
for i in range(1, N+1): # i는 자릿수
    if i == 1: # 1자리수 일 때는 임의로 "5"일때에 체크
        dp[i][2] = 1
    else:
        for j in range(3): # j는 자릿수를 모두 합한 나머지
            dp[i][(j+1)%3] += dp[i-1][j]
            dp[i][(j+5)%3] += dp[i-1][j]

print(dp[N][0]%1000000007)