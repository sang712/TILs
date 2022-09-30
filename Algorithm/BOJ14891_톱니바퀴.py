'''
시계방향으로 회전하면 맨 뒤의 값이 맨 앞으로 옴
톱니바퀴를 돌리는 함수를 만들어서 연결된 톱니바퀴가 돌아갈 것이면
해당 톱니바퀴를 정보를 담아 재귀로 함수를 호출하고
호출이 한번이라도 됐으면 어쨌든 돌려야 하므로 함수가 끝날 때 쯤에 돌리는 것으로 구현함
'''
# 톱니바퀴 상태, N극 0, S극 1, 0번 인덱스 12시, 시계방향 순서
cogs = ['']+[input() for _ in range(4)]

def rot_cog(cog, rot_d, d): # cog 번호, 회전 방향, 다음 cog 방향 왼쪽-1, 시작0, 오른쪽1
    if cog == 1:
        if d >= 0:
            if not cogs[1][2] == cogs[2][6]:
                rot_cog(2, -rot_d, 1)    
    elif cog == 2:
        if d >= 0:
            if not cogs[2][2] == cogs[3][6]:
                rot_cog(3, -rot_d, 1)
        if d <= 0:
            if not cogs[2][6] == cogs[1][2]:
                rot_cog(1, -rot_d, -1)
    elif cog == 3:
        if d >= 0:
            if not cogs[3][2] == cogs[4][6]:
                rot_cog(4, -rot_d, 1)
        if d <= 0:
            if not cogs[3][6] == cogs[2][2]:
                rot_cog(2, -rot_d, -1)
    elif cog == 4:
        if d <= 0:
            if not cogs[4][6] == cogs[3][2]:
                rot_cog(3, -rot_d, -1)
    cogs[cog] = cogs[cog][-1] + cogs[cog][:-1] if rot_d == 1 else cogs[cog][1:] + cogs[cog][0]
    
def solve():
    K = int(input())
    for _ in range(K):
        cog, rot_d = map(int, input().split())
        rot_cog(cog, rot_d, 0)
    ans = 0
    for i in range(4):
        ans += 2**i if cogs[i+1][0] == '1' else 0
    print(ans)
solve()