'''
people이라는 이름의 list로 input을 받고
길이 N의 rank라는 이름의 list에 등수를 넣어 문제에서 요구하는 대로 구현하였음
덩치가 작을 때 등수가 더해지는 것에 주의해야함
'''
N = int(input())

people = []
rank = [1] * N
for _ in range(N):
    people.append(tuple(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1

for num in rank:
    print(num, end=' ')