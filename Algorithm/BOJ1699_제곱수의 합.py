"""
처음 문제를 풀 때 루트를 씌워서 버림한 수와 조합을 해서 만드는 경우의 수만 생각했는데
이렇게 하면 12에서 틀린 답을 도출하게 됨
내 풀이로 하면 9 + 3 으로 4가 나오는데
답은 4 + 4 + 4 로 3이 나와야 함
그래서 풀이를 1부터 루트를 씌워 버림한 수까지 for문을 돌리면서
조합을 확인해보는 방식으로 수정하였음
"""
N = int(input())
dp = [0]
for i in range(1, N + 1):
    floor_root = int(i ** 0.5)
    if i == floor_root ** 2:
        dp.append(1)
        continue
    temp = set()
    for j in range(1, floor_root + 1):
        temp.add(dp[j ** 2] + dp[i - j ** 2])
    dp.append(min(temp))
print(dp[-1])