L, P = map(int, input().split())

public = list(map(int, input().split()))

print(*[num - L * P for num in public])