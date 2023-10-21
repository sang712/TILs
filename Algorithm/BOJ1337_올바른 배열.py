"""
인덱스 1이 증가할 때 값도 1이 증가하는 것으로 했다가 틀린 답을 제출할 뻔 했음
그게 아니라 인덱스가 증가할 때 그 숫자에 5를 더한 수 미만이면 카운팅을 하는 것으로 수정 했음
"""
N = int(input())

nums = [int(input()) for _ in range(N)]
nums.sort()

ans = 5
for i in range(N):
    num = nums[i]
    cnt = 0
    for j in range(min(N - i, 5)):
        if nums[i + j] <= num + 4:
            cnt += 1
    ans = min(ans, 5 - cnt)
print(ans)