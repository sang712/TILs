"""
에라토스테네스의 체를 이용해 103까지의 소수를 얻었고
N보다 큰 연속한 소수의 곱을 출력하였음
"""
N = int(input())
colander = [0] * 104
prime_nums = []
for i in range(2, 104):
    if colander[i]:
        continue
    prime_nums.append(i)
    for j in range(i, 104, i):
        colander[j] = 1
for i in range(1, len(prime_nums)):
    special_num = prime_nums[i] * prime_nums[i-1]
    if special_num > N:
        print(special_num)
        break