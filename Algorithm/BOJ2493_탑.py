"""
for문 안에서 stack이 반복되니 N*N으로 O(N^2)가 될 줄 알았는데
stack 자체는 pop을 하기 때문에
먼저 pop이 되든 나중에 pop이 되든 반복되는 총량은 같으므로
N * N 이 아닌 N + N이 되는 결과를 낳음
따라서 시간초과가 나지 않고 다음 코드로 시간내에 풀이가 가능함
for문으로 탑들을 돌면서 스택에 index와 높이를 집어넣고
스택의 탑들의 높이를 현재 for문의 탑의 높이와 비교하여 그보다 작으면 pop하고
(현재 탑보다 작은 탑에는 어차피 신호가 이 탑에 막혀 닿지 못할 것이기 때문에 pop을 함)
그보다 크면 답에 넣는 방식으로 스택의 크기를 줄이면서 for문을 반복함
"""
N = int(input())

towers = list(map(int, input().split()))

stack = []
ans = [0] * N
for i in range(len(towers)):
    while stack:
        receiver, height = stack.pop()
        if height > towers[i]:
            ans[i] = receiver + 1
            stack.append((receiver, height))
            break
    stack.append((i, towers[i]))
print(*ans)