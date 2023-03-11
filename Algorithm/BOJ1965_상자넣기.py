"""
상자를 넣는데에는 방향성이 있으므로
왼쪽에서 오른쪽으로 진행하고
이중 for문을 통해
해당 인덱스의 상자에 포함되는 상자의 개수를 dp에 담아 저장하였음
"""
n = int(input())
boxes = list(map(int, input().split()))
dp = [1] * n
for i in range(n - 1):
    for j in range(i + 1, n):
        if boxes[i] < boxes[j]:
            dp[j] = max(dp[i] + 1, dp[j])
            
print(max(dp))