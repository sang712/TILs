"""
while문에 right가 N에 도달하면 중단하도록 했는데 이렇게 하면 안 되고
누적합이 M보다 적어서 right을 증가시켰을 때 끝에 도달한 경우에 중단하도록 해야함

반례
5 12
1 1 1 1 10
오답 결과: 0
정답 결과: 1
"""
N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
current_sum = nums[0]
cnt = 0
while True:
    if current_sum < M:
        if right < N:
            current_sum += nums[right]
            right += 1
        else:
            break
    else:
        if current_sum == M:
            cnt += 1
        current_sum -= nums[left]
        left += 1
print(cnt)