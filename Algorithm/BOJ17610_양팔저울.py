"""
추를 물통과 같은 곳에 놓는 방법 
반대 방향에 놓는 방법 2가지를 모두 고려해서
만들 수 있는 물의 무게를 찾고
최댓값에서 개수를 빼서 출력하였음
"""
k = int(input())
gs = list(map(int, input().split()))

comb = set()
for g in gs:
    temp = []
    for c in comb:
        temp.append(g+c)
        temp.append(abs(g-c))
    comb.update(temp)
    comb.add(g)
comb.discard(0)
print(max(comb)-len(comb))