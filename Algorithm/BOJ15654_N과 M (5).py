'''
처음에 문제를 이해하길 순서대로 골라서 출력하는 줄 알았는데 
그게 아니라 순열을 출력하는 것이라 다시 처음부터 조사를 해야 했음
visited 변수를 설정해 구현하였음
'''
N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

perm = []
visited = [0] * N
def make_perm() -> None:
    if len(perm) == M:
        return print(*perm)
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        perm.append(nums[i])
        make_perm()
        visited[i] = 0
        perm.pop()
        
make_perm()