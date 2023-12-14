"""
for문을 돌면서 10의 계승인 수와 N과 비교하여 N이 더 크다면 
직전 수와 그 수까지의 수의 자릿수의 합을 하도록 하였음

입력으로 주어진 수가 1_000_000_000 미만이면 마지막에 체크한 n을 이용해서 상관 없는데
이상이되는 경우에는 n에 1이 더해져야해서 for문을 굳이 10번째까지 체크하도록 수정하였음
"""

N = int(input())

ans = 0
last_counted_num = 0
for n in range(1, 11):
    if N >= 10 ** n:
        ans += 9 * n * 10 ** (n - 1) 
        last_counted_num += 9 * 10 ** (n - 1)
    else:
        break
ans += (N - last_counted_num) * n

print(ans % 1234567)