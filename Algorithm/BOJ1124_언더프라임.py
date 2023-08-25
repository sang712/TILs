"""
소수 중 가장 작은 수인 2로만 수를 만든다고 하면 제한조건인 10만 이상이 되는 수는 2^17인 13만이고
따라서 될 수 있는 언더프라임의 소수의 개수는 17보다 작은 소수인 13개가 최대임
문제의 조건에서도, 소인수 분해에서도 쓸 수 있는 소수는 먼저 저장해 두었고
그보다 큰 소수로 이루어진 수를 소인수 분해할 때는 에라토스테네스의 체 방식을 이용해서 계산하도록 하였음
for문을 돌면서 while로도 구현해봤는데 오히려 80ms가 더 걸려서 해당 부분은 다시 원복하였음
"""
prime_num = {2, 3, 5, 7, 11, 13}

A, B = map(int, input().split())
ans = 0
for n in range(A, B + 1):
    cnt = 0
    while n > 1:
        for i in prime_num:
            if n % i == 0:
                n //= i
                cnt += 1
                break
        else:
            for i in range(max(prime_num), int(n ** 0.5) + 1):
                if n % i == 0:
                    n //= i
                    cnt += 1
                    break
            else:
                cnt += 1
                break
    if cnt in prime_num:
       ans += 1
print(ans)