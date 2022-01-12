N = int(input())
shelf = []
for _ in range(N):
    shelf.append(int(input()))

last_left = 0
last_right = 0
left = 0
right = 0
for i in range(N):
    if last_left < shelf[i]:
        last_left = shelf[i]
        left += 1

    if last_right < shelf[N-1-i]:
        last_right = shelf[N-1-i]
        right += 1

print(left)
print(right)