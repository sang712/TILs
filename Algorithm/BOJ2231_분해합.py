N = int(input())

const = 54 # N은 백만까지, N 미만의 수는 6자리라 최소 6*9보다 작은 숫자부터 만족함
starting_number = N-const if N-const > 0 else 0
is_found = False
for i in range(starting_number, N):
    num = i
    sum = num
    while num:
        sum += num%10
        num //= 10

    if sum == N:
        print(i)
        is_found = True
        break
if not is_found:
    print(0)