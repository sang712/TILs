"""
정렬을 하면 되는 문제인 줄 알았는데 주사위의 입체적인 모양을 고려하지 않았기 때문
서로 나올 수 있는 세 면의 쌍과 두 면의 쌍이 정해져 있으므로
해당 쌍들을 구해서 해당 면의 합의 최소를 각각 구하였고
마지막에 해당되는 면들이 얼마큼 나오는지 계산하여 더해주었음

두 면의 쌍을 구할 때 i > 2이면 return하는 부분을 append하는 부분보다 우선하여
모든 조합이 나오지 않아서 틀린답을 제출하였었음
"""
N = int(input())
dice = list(map(int, input().split()))

opposite_sides = [(0, 5), (1, 4), (2, 3)]
sides_of_3 = []
def comb_3(temp):
    i = len(temp)
    if i == 3:
        sides_of_3.append(temp.copy())
        return
    for j in range(2):
        temp.append(opposite_sides[i][j])
        comb_3(temp)
        temp.pop()        
comb_3([])

sides_of_2 = []
def comb_2(temp, i):
    if len(temp) == 2:
        sides_of_2.append(temp.copy())
        return
    if i > 2:
        return
    for j in range(2):
        temp.append(opposite_sides[i][j])
        comb_2(temp, i + 1)
        temp.pop()
    comb_2(temp, i + 1)
comb_2([], 0)

min_3_sides = []
for i, j, k in sides_of_3:
    min_3_sides.append(dice[i] + dice[j] + dice[k])

min_2_sides = []
for i, j in sides_of_2:
    min_2_sides.append(dice[i] + dice[j])
    
ans = 0
if N == 1:
	ans = sum(dice) - max(dice)
else:
	ans += 4 * min(min_3_sides)
	ans += (8 * (N - 2) + 4) * min(min_2_sides)
	ans += (5 * (N - 2) + 4) * (N - 2) * min(dice)
print(ans)