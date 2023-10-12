import sys
input = sys.stdin.readline

def find_m(candidate):
    mods = set()
    for student in students:
        mods.add(student % candidate)
        
    if len(mods) == G:
        return True
    return False

for tc in range(int(input())):
    G = int(input())
    
    students = [int(input()) for _ in range(G)]

    for i in range(G, 1_000_000):
        if find_m(i):
            print(i)
            break
