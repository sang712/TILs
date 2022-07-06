def calculate(X):
    a, b, c = -1, -1, -1
    if X % 3 == 0:
        a = X // 3
    if X % 2 == 0:
        b = X // 2
    c = X - 1
    return [a, b, c]

N = int(input())

dp = [set(int(input()))]

for nums in range(dp):
    temp = set()
    for num in nums:
        a, b, c = calculate(num)
        if a > 0: temp.add(a)
        if b > 0: temp.add(b)
        if c > 0: temp.add(c)
        if a == 1 or b == 1 or c == 1:
            pass
    dp.append(temp)
    