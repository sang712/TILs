"""
막상 보고 어려워했었는데 풀어보니 생각보다 쉬운 문제였음
주어진 수를 for문으로 돌고
줄 세울 리스트를 다시 for문으로 돌면서
줄 세울 리스트의 빈 부분의 개수를 세면서 이 수가 입력과 같으면 그 공간에 수를 채워넣는 식으로 풀이하였음
"""
N = int(input())
order = list(map(int, input().split()))

line = [0] * N
for i in range(N):
    cnt_0 = 0
    for j in range(N):
        if line[j] == 0:
            if order[i] == cnt_0:
                line[j] = i + 1
                break
            cnt_0 += 1
print(*line)