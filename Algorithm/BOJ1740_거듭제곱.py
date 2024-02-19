"""
3의 거듭 제곱을 한 번씩 쓰거나 안 쓰기 때문에 비트연산을 생각했고
주어진 수를 2진화 한 뒤에 그 수를 그대로 3진수로 생각하고 10진화를 하는 방식으로 풀이하였음
"""
N = int(input())

nums = []
while N:
    N, mod = divmod(N, 2)
    nums.append(mod)

ans = 0
for num in nums[::-1]:
    ans *= 3
    ans += num
print(ans)