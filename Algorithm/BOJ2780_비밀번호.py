"""
서로 인접한 수를 딕셔너리 자료 구조에 넣고 인접한 수를 쉽게 참조할 수 있도록 하였음
비밀번호의 길이가 늘어나면서 특정 번호로 끝날 경우의 수는
비밀번호 길이가 1 짧으면서 그 번호에 인접한 번호들을 마지막으로 선택한 경우의 수의 합과 같으므로 
dp 방식을 이용해 풀이하였음
"""
adjacent = {1: [2, 4], 2: [1, 3, 5], 3: [2, 6], 4: [1, 5, 7], 5: [2, 4, 6, 8], 
            6: [3, 5, 9], 7: [4, 8, 0], 8: [5, 7, 9], 9: [6, 8], 0: [7]}

T = int(input())
l_password = [int(input()) for _ in range(T)]

dp = [[1] * 10]
for i in range(max(l_password)):
    temp = [0] * 10
    for key in adjacent:
        for num in adjacent[key]:
            temp[key] += dp[i][num]
        temp[key] %= 1234567
    dp.append(temp)
ans = [sum(dp[l_password[i]-1])%1234567 for i in range(T)]
print(*ans)