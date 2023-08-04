N = int(input())
skills = input()

ans = 0
skill_without_num = []
for skill in skills:
    if '1' <= skill <= '9':
        ans += 1
    else:
        skill_without_num.append(skill)

Ss = 0
Ls = 0
for skill in skill_without_num:
    if skill == 'S':
        Ss += 1
    elif skill == 'L':
        Ls += 1
    elif skill == 'K' and Ss:
        Ss -= 1
        ans += 1
    elif skill == 'R' and Ls:
        Ls -= 1
        ans += 1
    
print(ans)
    