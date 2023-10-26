N = int(input())
F = int(input())

for i in range(100):
    num = (N // 100) * 100 + i
    if num % F == 0:
        print(i if i >= 10 else '0' + str(i))
        break