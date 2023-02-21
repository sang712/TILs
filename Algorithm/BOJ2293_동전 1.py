"""
전형적인 dp문제라 하여 풀게 되었음
브루트포스를 적용해도 되는 dp문제라고 생각해서
2중 for문에 dp의 idx를 우선으로 배치했었는데
이렇게 되면 동전의 단위에 따라 구분되지 않으면서 진행되게 되고
결과적으로 같고 순서가 다른 경우를 따로 캐치해내지 못하는 문제가 발생하게 됨

그래서 for문에 동전의 단위를 먼저 적용하도록 하였더니 중복이 되는 경우를 거를 수 있었음
처음에는 단위의 크기도 중요하다고 생각해서 정렬을 적용하였는데
거꾸로 해도 같은 결과가 나왔기에 단위는 중요하지 않고
dp를 계산할 때 한 단위의 동전만을 계산하고 다음 동전을 계산해야한다는 것을 알 수 있었음

그리고 문제에서 제시했던 동전의 단위는 k보다 큰 100_000이 될 수 있다는 점을 간과하여
index에러가 났었는데 해당 문제는 k보다 큰지 작은지 비교하여 해당 부분을 제외 하였음

아예 nums에 num을 넣을 때 k보다 큰지 확인하였더니 오히려 시간이 증가하였음
그래서 그냥 첫 제출시의 코드로 제출하였음
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (k + 1)
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)
    
for num in nums:
    if num <= k:
        dp[num] += 1
    else:
        continue
    
    for i in range(1, k + 1):
        if num + i <= k:
            dp[i + num] += dp[i]

print(dp[k])