"""
개미수열을 만들어보면 규칙상 3을 초과하는 수는 나올 수 없으므로
3이 나오는 항부터는 최대가 무조건 3이기 때문에
그냥 하드 코딩하여 문제를 해결하였음

직접 구하려니 시간초과가 났음
"""
N = int(input())

print(1 if N <= 2 else 2 if N <= 5 else 3)

# ant = ['', '1']
# for _ in range(N-1):
#     last = ant[-1]
#     curr = []
#     serial_num, cnt = last[0], 0
#     for num in last:
#         if serial_num == num:
#             cnt += 1
#             continue
#         curr.append(serial_num)
#         curr.append(str(cnt))
#         serial_num = num
#         cnt = 1
#     curr.append(serial_num)
#     curr.append(str(cnt))
#     serial_num = num
#     cnt = 1
#     ant.append(''.join(curr))
# print(max(ant[-1]))