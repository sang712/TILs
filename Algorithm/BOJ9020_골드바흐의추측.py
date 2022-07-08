# pypy3 2.4초 통과

prime = [2]
for i in range(3, 10001, 2):
    for p_num in prime:
        if i%p_num == 0:
            break
        elif p_num == prime[-1]:
            prime.append(i)

for tc in range(1, int(input())+1):
    N = int(input())
    out = ''
    for i in prime:
        if i > N//2:
            break
        for j in prime:
            if i+j > N:
                break
            elif i+j == N:
                out = f'{i} {j}'
    print(out)

# python3 0.5초 통과
# n = 10000
# num_list = [True] * n
# for i in range(2, int(n ** 0.5) + 1):
#     if num_list[i]:
#         for j in range(2 * i, n, i):
#             num_list[j] = False
# 
# for _ in range(int(input())):
#     n = int(input()) // 2
#     i = 0
#     while not (num_list[n - i] and num_list[n + i]):
#         i += 1
#     print(n - i, n + i)