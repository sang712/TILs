'''
완전 탐색에 백트래킹을 섞어서 구현하였음
구현한 함수에 전달되는 perm 리스트는 얕은 복사가 된 것이기 때문에
길이가 M보다 길면 pop을 한번 더 해주는 방향으로 진행하였음
'''
N, M = map(int, input().split())

def solve(perm, num):
    if num > N:
        return
    perm.append(str(num))
    if len(perm) == M:
        print(' '.join(perm))
    elif len(perm) > M:
        perm.pop()
        return
    solve(perm, num + 1)
    perm.pop()
    solve(perm, num + 1)
solve([], 1)
        