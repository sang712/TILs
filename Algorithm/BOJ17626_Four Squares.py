'''
n을 합으로 표현하기 위한 제곱수의 최소의 개수를 dp형태로 만들어서 구현하였음
우선 제곱수들의 합을 dp로 저장하기 위해서 1부터 n + 1까지 순차적으로 i로 for문으로 돌고
그 후에 1부터 i의 제곱근까지 j로 한 번 더 for문을 돌면서
i에 j의 제곱수를 뺀 경우의 dp값인 comb_of_squares[i - j ** 2] 값 중 가장 작은 값을 결정해서
(직전 값과 비교했는데 이렇게 되면 누적된 min값이 의미없어지고 추가적으로 직전 값은 j가 1일 때 이미 체크하게 됨)
dp에 저장함

+) 그런데 dp로 시간초과 나서 브루트 포스로 풀었음

+) 문제를 잘 읽으면 알 수 있는 사실이 아무리 많은 제곱수를 사용하더라도 최대 4개까지만 필요함
그래서 n의 제곱근이 정수일 때,
for i로 n - i ** 2 의 제곱근이 정수일 때
for i, for j로 n - i ** 2 - j ** 2 의 제곱근이 정수일 때
그 외의 경우
총 4가지의 경우로 나누어 브루트 포스하게 문제를 풀 수 있음
56ms 소요
'''
n = int(input())

def four_squares(n):
    if int(n**0.5) == n**0.5:
        return 1
    for i in range(1, int(n**0.5) + 1):
        if int((n - i**2)**0.5) == (n - i**2)**0.5:
            return 2
    for i in range(1, int(n**0.5) + 1):
        for j in range(1, int((n - i**2)**0.5) + 1):
            if int((n - i**2 - j**2)**0.5) == (n - i**2 - j**2)**0.5:
                return 3
    return 4

print(four_squares(n))

# 더 빠른 풀이 36ms
'''
def solution(N):
    if (N**.5).is_integer(): return 1

    set_1 = {i**2 for i in range(int(N**.5),0,-1)} # N 이하 제곱수들
    for i in set_1:
        if N-i in set_1: return 2
    
    while N%4==0:
        N //= 4    
    return 4 if N%8==7 else 3

print(solution(int(input())))
'''