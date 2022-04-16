N, M = map(int, input().split())
arr = []

arr += list(map(int, input().split()))
arr += list(map(int, input().split()))

arr.sort()
# arr = sorted(arr) # 아니면 이 방식

print(*arr)