N, K = map(int, input().split())
A = list(map(int, input().split()))

done = [0] * N

count = 0
def WorkOut(day, weight):
    global count

    if weight < 500:
        return
    if day >= N:
        count += 1
        return

    for i in range(N):
        if done[i]:
            continue
        done[i] = 1
        WorkOut(day + 1, weight + A[i] - K)
        done[i] = 0

WorkOut(0, 500)
print(count)