N, K = map(int, input().split())

num_list = []
for i in range(1, K+1):
    num = N * i
    reversed_num = 0
    while num:
        reversed_num *= 10
        reversed_num += num % 10
        num //= 10
    num_list.append(reversed_num)

print(max(num_list))