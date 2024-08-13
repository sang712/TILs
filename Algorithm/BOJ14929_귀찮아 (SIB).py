"""
일일이 다 곱하면 O(n^2) 이라 시간 초과가 나기 때문에
덧셈의 분배법칙을 이용해 모든 수를 다 더한 뒤 곱해야 할 수만 빼면서
답에 누적시켰음
"""
n = int(input())
nums = list(map(int, input().split()))
ans = 0
sumation = sum(nums)
for num in nums:
    sumation -= num
    ans += num * sumation
print(ans)