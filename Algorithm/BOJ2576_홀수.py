min_num = 101
sumation = 0
for _ in range(7):
    num = int(input())
    if num % 2:
        sumation += num
        min_num = min(min_num, num)
if sumation:
    print(sumation)
    print(min_num)
else:
    print(-1)
