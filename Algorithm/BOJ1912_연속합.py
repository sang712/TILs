"""
실버2임에도 불구하고 생각해내기 어려웠던 문제
다이나믹 프로그래밍으로 푸는 문제였는데 dp안에 무엇을 넣느냐를 생각해내기 어려웠음
dp에는 해당 index 번째 까지 수의 수열 중 가장 합이 큰 부분 수열의 합을 넣음
말로 풀어 쓰니 엄청 길어졌는데
코드는 매우 간단함
dp에 수열의 첫 수를 먼저 넣고
dp의 마지막 값과 수열의 다음 수를 더한 값과, 수열의 다음 수를 비교하여 더 큰 수를 dp에 저장하면
위의 4번째 줄에 서술된 값이 저장이 되게 됨
그 후에 가장 큰 수를 찾아서 출력하도록 하였음
쉽게 설명하면 이전 값과 현재 값을 더하는 것 중 더 큰 값을 dp에 저장하게 되면
값이 커지는 경우에만 덧셈이 되고 그렇지 않는 경우에는 중단이 되는 과정이 반복되게 됨
"""
n = int(input())
nums = list(map(int, input().split()))

dp = [nums[0]]
for i in range(1, n):
    dp.append(max(dp[i-1] + nums[i], nums[i]))
print(max(dp))