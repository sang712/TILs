"""
문제에서 요구하는 사항을 구현하기 위해
각 레인을 돌면서 오른쪽에 가장 가까운 카누를 찾도록 하였고
숫자가 없으면 무시하도록 하였음

그 후에 그 결과 값을 이용해 정렬을 하여
등수를 매겼고 해당 등수를 출력하였음
"""
R, C = map(int, input().split())

rane = [input() for _ in range(R)]

dist = [51] * 10

for i in range(R):
    c = C - 2
    cnt = 0
    while c:
        if rane[i][c] == '.':
            cnt += 1
            c -= 1
            continue
        elif rane[i][c].isdigit():
            canoe = int(rane[i][c])
            dist[canoe] -= cnt
        break
    
comparing = sorted([(i, dist[i]) for i in range(1, 10)], key=lambda x: x[1], reverse=True)
ranks = [0] * 9
rank = 1
ranks[comparing[0][0] - 1] = rank
for i in range(1, 9):
    canoe, dist = comparing[i]
    if dist != comparing[i-1][1]:
        rank += 1
    ranks[canoe - 1] = rank

print(*ranks, end='\n')