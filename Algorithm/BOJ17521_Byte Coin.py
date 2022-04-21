n, W = map(int, input().split())

minmax = []
for i in range(n):
    s = int(input())
    if i == 0 or i == 1:
        minmax.append(s)
    else:
        last = minmax[-1]
        secondToLast = minmax[-2]
        if last - secondToLast >= 0: # 증가할 때
            if last > s: # 다음 가격이 떨어지면
                minmax.append(s)
            else: # last <= s 다음 가격이 올라가면
                minmax[-1] = s
        elif last - secondToLast < 0: # 감소할 때
            if last > s: # 다음 가격이 떨어지면
                minmax[-1] = s
            else: # last <= s 다음 가격이 올라가면
                minmax.append(s)
i = 0
while i < len(minmax)-1:
    if minmax[i+1] > minmax[i]:
        coins = W // minmax[i]
        W %= minmax[i]
        W += coins * minmax[i+1]
    i += 1
print(W)