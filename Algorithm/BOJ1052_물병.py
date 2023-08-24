"""
10^7은 천만이고 2의 지수로 24승을 하면 천만을 초과하므로 해당 길이의 비트를 마스킹하는 리스트를 만들었음
그리고 비트로 계산해서 저장하였고
그리고 1인 비트들의 합이 K이하이도록
반복문으로 비트에 1을 더하면서 K를 하나씩 빼도록 하였고
비트에 1을 더할 때 해당 비트에 해당하는 숫자를 모두 더해 저장하여 출력하였음
"""
N, K = map(int, input().split())

bottles = [0] * 25
cnt = 0
for i in range(24, -1, -1):
    bottle = 2 ** i
    if N >= 2 ** i:
        N -= bottle
        bottles[i] += 1
        cnt += 1
ans = 0
while cnt > K:
    start = 25
    for i, bottle in enumerate(bottles):
        if bottle:
            ans += 2 ** i
            start = i
            bottles[i] += 1
            cnt += 1
            break
    for j in range(start + 1, 25):
        if bottles[j - 1] == 2:
            bottles[j - 1] = 0
            bottles[j] += 1
            cnt -= 1
        else:
            break
print(ans)