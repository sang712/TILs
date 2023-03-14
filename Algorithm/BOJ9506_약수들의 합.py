while True:
    n = int(input())
    if n == -1:
        break
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    divisors.remove(n)
    divisors = list(divisors)
    divisors.sort()
    if sum(divisors) == n:
        print(f'{n} = ', end='')
        print(*divisors, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')