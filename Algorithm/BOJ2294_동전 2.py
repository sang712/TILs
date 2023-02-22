"""
이것도 또한 전형적인 dp문제이기 때문에 풀게 되었음

사용한 동전의 개수를 출력하는 경우라 
경우의 수를 출력하는 BOJ2293 동전 1 문제와는 다르게 dp를 이용할 필요가 있었음

그래서 고민한 결과 금액을 idx로 갖는 것은 BOJ2293 문제와 동일하되
갖고 있는 값은 사용한 동전의 개수로 dp를 설정하였음
그러고나서 동전을 기준으로 for문을 돌면서
dp[i] + 1과 dp[i + num]을 비교해서 작은 값을 갖도록 하였고
dp[k] 값이 갱신 되지 않았을 때는 -1을 출력하도록 하였음

그리고 리스트에 -1을 담든 10001을 담든 소요하는 메모리는 같기 때문에
10001을 담는 것으로 수정하여 코드 길이를 줄였으며
if 문으로 거르는 것을 없애니 시간도 100ms 단축할 수 있었음
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

nums = []
for _ in range(n):
    num = int(input())
    if num <= k:
        nums.append(num)
    
dp = [10001] * (k + 1)

for num in nums:
    dp[num] = 1
    for i in range(1, k + 1):
        if num + i > k:
            break
        dp[i + num] = min(dp[i + num], dp[i] + 1)
print(dp[k] if dp[k] < 10001 else -1)