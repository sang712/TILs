dwarves = [0 for _ in range(9)]

for i in range(9):
    dwarves[i] = int(input())

total = sum(dwarves)

isBreak = False
for i in range(8, 0, -1):
    for j in range(i-1, -1, -1):
        if total - dwarves[i] - dwarves[j] == 100:
            dwarves.pop(i)
            dwarves.pop(j)
            isBreak = True
            break
    if isBreak:  break

dwarves = sorted(dwarves)

for dwarf in dwarves:
    print(dwarf)