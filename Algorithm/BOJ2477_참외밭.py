"""
일부러 찾아서 푼 첫 기하학문제
어떻게 풀까 고민을 많이 했는데
방향이 연속으로 두번 반복되는 경우에 반복되는 중간 부분이 안으로 파고드는 부분임을 파악해서
가장 큰 가로와 세로를 곱한 것에서 해당 부분을 곱한 것을 빼는 방식으로 구현하였음

예를 들어
방향이
3 -> 1 -> 3 -> 1 -> 4 -> 2 라면
마지막에 사용된 두 길이를 곱한 것에서 두번째와 세번째에 사용된 길이를 곱한 것을 뺐고
1 -> 3 -> 1 -> 4 -> 2 -> 3 이라면
원형 탁자를 돌리듯이 넘기면서 위의 예시를 만들어 풀었음

구현하는 것은 어렵지 않았지만 생각을 좀 하게하는 문제였기 때문에 재미있는 문제였음
"""
num_oriental_melon = int(input())

order = [list(map(int, input().split())) for _ in range(6)]
area = 0

for _ in range(4):
    if area:
        break
    for i in range(3):
        if order[i][0] == order[i + 2][0] and order[i + 1][0] == order[i + 3][0]:
            temp = order[:i] + order[i + 4:]
            area = temp[0][1] * temp[1][1] - order[i + 1][1] * order[i + 2][1]
            break
    else:
        order = order[1:] + order[:1]
print(area * num_oriental_melon)