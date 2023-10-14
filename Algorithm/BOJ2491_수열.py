N = int(input())
nums = list(map(int, input().split()))

cnt, last_num = 0, 0
ans = 0
for n in nums:
    if n >= last_num:
        cnt += 1
    else:
        cnt = 1
    last_num = n
    if ans < cnt:
        ans = cnt

cnt, last_num = 0, 0
for n in nums:
    if n <= last_num:
        cnt += 1
    else:
        cnt = 1
    last_num = n
    if ans < cnt:
        ans = cnt

print(ans)