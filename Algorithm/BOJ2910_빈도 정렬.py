"""
람다식으로 정렬할 때 사용하는 키와 우선순위를 주어 구현하였음
"""
N, C = map(int, input().split())

counter = {}
for i, num in enumerate(map(int, input().split())):
    counter.setdefault(num, [0, i])
    counter[num][0] += 1
ans = []
for num, info in sorted(list(counter.items()), key=lambda x: (-x[1][0], x[1][1])):
    ans.extend([num] * info[0])

print(*ans)