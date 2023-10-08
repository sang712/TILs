"""
에라토스테네스의 체를 적용하여 문제 시간을 크게 단축할 수 있었음
원래 시도했던 풀이는 매번 이전에 나왔던 소수로 나눠보는 것이었는데
에라토스테네스의 체 방법은 소수로 판정이 되었다면 그 수에 배수에 해당하는 수를 제거하는 방식으로 하기 때문에
소수의 개수가 늘어날 때마다 증가하는 나눗셈 연산을 그리 많이 할 필요가 없음

"while temp_max >= 1:" 에서 같은 경우를 포함하지 않아서
5 8 이라는 입력에 0이라는 틀린 출력을 내보내는 것을 확인하였음
"""
A, B = map(int, input().split())

end = int(B ** 0.5) + 1
colander = [0, 0] + [1] * (end - 1)
prime_number = []
for i in range(2, end):
    if colander[i]:
        prime_number.append(i)
        for j in range(2 * i, end, i):
            colander[j] = 0

cnt = 0    
for prime in prime_number:
    almost_prime = prime * prime
    while almost_prime < A:
        almost_prime *= prime
        
    temp_max = B / almost_prime
    while temp_max >= 1:
        cnt += 1
        temp_max /= prime
print(cnt)