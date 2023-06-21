N = int(input())
files = map(int, input().split())
cluster = int(input())

ans = 0
for file in files:
    if file:
        cnt, file = divmod(file, cluster)
        if file:
            cnt += 1
        ans += cnt * cluster
print(ans)
