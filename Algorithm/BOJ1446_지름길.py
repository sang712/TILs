"""
뭔가 정돈되지 않는 느낌이지만 bfs방식과 유사하게 풀이하였음
"""
N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]
shortcuts.sort()

def takingroad(pos, dist, i):
    if pos > D:
        return 120001
    if i >= N:
        if pos <= D:
            return dist + D - pos
        else:
            return 120001
    
    takein, takeout, d = shortcuts[i]
    taking = 120001
    if pos <= takein:
        taking = takingroad(takeout, takein - pos + dist + d, i+1)
    nottaking = takingroad(pos, dist, i+1)
    
    return min(taking, nottaking)

print(takingroad(0, 0, 0))