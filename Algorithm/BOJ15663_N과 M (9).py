"""
수열 리스트를 함수의 인자로 받지 않고 그냥 밖에다 선언해서 사용하는 방법을 이용해 보았음
수열 문제는 풀면 쉬운데 풀이 과정을 깔끔하게 하려다보니 살짝 뇌정지가 오는 경향이 있음
조금 더 연습해서 그냥 dfs, bfs, 이분탐색 문제 풀듯이 익숙해져야겠음
"""
N, M = map(int, input().split())
nums = list(map(int, input().split()))

ans = set()
visited = [0] * N
temp = []
def sequence():
    if len(temp) == M:
        ans.add(tuple(temp))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            temp.append(nums[i])
            sequence()
            temp.pop()
            visited[i] = 0
sequence()
for case in sorted(list(ans)):
    print(*case)