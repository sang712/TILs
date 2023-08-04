"""
포인트는 중간에 스킬 연계에 실패하면 그 이후의 스킬 모두가 발동되지 않는다는 점이며
직전에 사용한 연계 사전 스킬이 어떤 것이였느냐와는 무관하다는 점이다
"""
N = int(input())
skills = input()

ans = Ss = Ls = 0
for skill in skills:
    if '1' <= skill <= '9':
        ans += 1
    elif skill == 'S':
        Ss += 1
    elif skill == 'L':
        Ls += 1
    elif skill == 'K':
        if Ss:
            Ss -= 1
            ans += 1
        else:
            break
    elif skill == 'R':
        if Ls:
            Ls -= 1
            ans += 1
        else:
            break
    
print(ans)
