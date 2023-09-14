"""
주어진 입력을 정렬한 뒤에 가장 처음 만나는 값을 저장하고
저장한 값에 L을 더해 그 값을 초과할 때마다 
저장 값을 새로 초기화하고 카운팅을 추가하는 방식으로 풀이하였음
"""
N, L = map(int, input().split())

leaks = list(map(int, input().split()))
leaks.sort()

num_tape = 1
amend = leaks[0]
for leak in leaks:
    if leak > amend + L - 1:
        amend = leak
        num_tape += 1
print(num_tape)