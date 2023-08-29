"""
배낭문제 방식으로 풀었고
풀이가 기억나지 않아 예전에 풀었던 문제를 참고하여 풀이하였음

문제의 입력에 따라 i와 j의 범위, 시작할 때의 0의 유무등을 유의하여 풀이해야함
"""

N = int(input())

people = zip(map(int, input().split()), map(int, input().split()))
sejun = [[0] * 100]

for i, person in enumerate(people):
    hp, joy = person
    greeting = []
    for j in range(100):
        if hp > j:
            greeting.append(sejun[i][j])
        else:
            greeting.append(max(sejun[i][j], sejun[i][j - hp] + joy))
    sejun.append(greeting)

print(sejun[N][99])