'''
4800ms나 걸린 내 코드에 비해 40배나 빠른 120ms가 걸린 코드
사람을 선택하고 각각의 시너지 만큼 더한다는 고민을 하지 않고
그냥 행 다 더하고, 열 다 더해서 그걸 한 사람의 몫으로 하였음
어쨌든 행, 열을 다 더해서 뽑은 사람의 값을 더하면 뽑은 사람의 값만 N/2배로 곱해지기 때문에
팀간의 차이를 계산할 때 없어지므로 선택한 방향
+) zip은 iterable한 객체의 원소를 튜플로 묶는 효과가 있음 ex) [[1, 2], [3, 4]] -> [(1, 3), (2, 4)]
++) list(zip(*2차원행렬))하면 원소가 튜플이면서 트랜스 포즈된 list(zip)을 얻을 수 있음
+++) 즉 zip(2차원행렬, zip(*2차원행렬))은 N*N정방행렬에 대해서 
N번째의 원소로 ([행], (열)) 튜플을 갖는 zip을 말함
allstat을 2로 나눈 이유는 전체 원소들이 2번씩 더해졌기 때문이고
newstat[:-1]에서 마지막 원소를 고려를 안 하는 이유는 마지막 원소를 고려 안하고 팀을 짜도
마지막 원소가 포함된 팀은 항상 반대팀이 되기 때문에
ex)123, 124, 125, 234, 235, 345 전부 6이 빠졌음을 알 수 있지만 상대팀에 있음
allstat에서 combi의 합을 빼도 되는 이유는 allstat에는 모든 원소가 1개씩 더해져 있고
combi의 합에는 팀에 포함된 원소는 무조건 2번씩 들어가 있고 그 외에는 1번씩이므로
ex)
▨▨▨▨▨▨   ㅁㅁㅁ▨▨▨   ▨▨▨ㅁㅁㅁ   ㅁㅁㅁㅁㅁㅁ
▨▨▨▨▨▨   ㅁㅁㅁ▨▨▨   ▨▨▨ㅁㅁㅁ   ㅁㅁㅁㅁㅁㅁ
▨▨▨▨▨▨ - ㅁㅁㅁ▨▨▨ = ▨▨▨ㅁㅁㅁ - ㅁㅁㅁㅁㅁㅁ
▨▨▨▨▨▨   ▨▨▨▩▩▩   ㅁㅁㅁㅁㅁㅁ   ㅁㅁㅁ▧▧▧
▨▨▨▨▨▨   ▨▨▨▩▩▩   ㅁㅁㅁㅁㅁㅁ   ㅁㅁㅁ▧▧▧
▨▨▨▨▨▨   ▨▨▨▩▩▩   ㅁㅁㅁㅁㅁㅁ   ㅁㅁㅁ▧▧▧
'''
import sys
from itertools import combinations as cb
N = int(sys.stdin.readline()) // 2
M = 2*N
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
allstat = sum(newstat) // 2
mins = 65535
for l in cb(newstat[:-1], N):
    mins = min(mins, abs(allstat - sum(l)))
print(mins)