"""
주어진 제한 조건이 작아서 수열을 일일이 구하는 방식으로 구현하였음
"""
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = set()

temp = []
def make_permutation(i):
    if len(temp) == M:
        ans.add(tuple(temp))
        return
    temp.append(nums[i])
    for j in range(i, N):
        make_permutation(j)
    temp.pop()
    
for i in range(N):
    make_permutation(i)
    
for perm in sorted(list(ans)):
    print(*perm)