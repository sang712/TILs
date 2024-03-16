"""
범위의 최댓값을 같은 수로 계속해서 나누는 방식으로 해당 범위에 해당 수가 인수로 몇 번 들어가있는지 계산했음
"""
n, m = map(int, input().split())

def num_factor(num, factor):
    cnt = 0
    while num:
        num //= factor
        cnt += num
    return cnt

two, five = num_factor(n, 2), num_factor(n, 5)
two -= num_factor(m, 2) + num_factor(n-m, 2)
five -= num_factor(m, 5) + num_factor(n-m, 5)

print(min(two, five))