N, B, H, W = map(int, input().split())

min_price = B + 1
for _ in range(H):
	p = int(input())
	a = list(map(int, input().split()))
	if N * p <= B:
		for i in a:
			if i >= N:
				min_price = min(min_price, N * p)
				break

print(min_price if min_price < B else "stay home")