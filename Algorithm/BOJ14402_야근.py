import sys
input = sys.stdin.readline

q = int(input())

commuting_list = {}
night_overtime = 0
for _ in range(q):
    name, commuting = input().split()
    commuting_list.setdefault(name, 0)
    if commuting == '+':
        commuting_list[name] += 1
    elif commuting == '-':
        if commuting_list[name] == 0:
            night_overtime += 1
        else:
            commuting_list[name] -= 1

night_overtime += sum(commuting_list.values())
print(night_overtime)