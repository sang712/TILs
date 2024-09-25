"""
피자를 가장 많이 원하는 사람만큼 기다리는 줄을 돌면서
피자를 더 원하면 줄을 선 것으로 간주해 줄 선 숫자를 하나씩 늘리고
만약 원하는 피자의 수가 1개라면 해당 줄까지의 피자 개수를 저장함
그리고 피자 개수를 하나씩 빼는 방식으로 구현하였음
"""
N = int(input())
people = list(map(int, input().split()))
order = [0] * N
need_pizza = N
cnt = 0
for b in range(max(people)):
    for i in range(N):
        if people[i] > 0:
            cnt += 1
        if people[i] == 1:
            order[i] = cnt
        people[i] -= 1
print(*order)
