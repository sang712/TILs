"""
예제 4번에서 확인해봐야하는 건 11까지가 아니라 23까지라는 것을 확인함

인자를 딥카피해서 전달하는 것 보다 해당 자료 구조를 그대로 쓰면서 append, pop하는 것이
시간 절약이 더 됨
"""
note = {'A': 1, 'A#': 2,'B': 3, 'C': 4, 'C#': 5, 'D': 6, 
        'D#': 7, 'E': 8, 'F': 9, 'F#': 10, 'G': 11, 'G#': 0}

N, M = map(int, input().split())
tunes = list(map(lambda x: note[x], input().split()))
cord = set(map(lambda x: note[x], input().split()))

ans = set()
def check_cord(tune_idx, candidate, fret):
    if 0 in ans:
        return
    
    if tune_idx >= N:
        if set(candidate) == cord:
            if fret:
                ans.add(max(fret) - min(fret) + 1)
            else:
                ans.add(0)
        return
    
    tune = tunes[tune_idx]
    if tune in cord:
        candidate.append(tune)
        check_cord(tune_idx + 1, candidate, fret)
        candidate.pop()
    
    for press_fret in range(1, 23):
        fretted_tune = (tune + press_fret) % 12
        if fretted_tune in cord:
            candidate.append(fretted_tune)
            fret.append(press_fret)
            check_cord(tune_idx + 1, candidate, fret)
            candidate.pop()
            fret.pop()

check_cord(0, [], [])
print(0 if 0 in ans else min(ans - {0, }))
"""
def f(string_idx, result):
    if len(result) == n:
        for i in visited:
            if i == 0:
                return
        else:
            if max(result) == 0 and min(result) == 0:
                ans.append(0)
            else:
                sorted_result = sorted(result)
                tmp = []
                max_result = sorted_result[-1]
                min_result = 0
                for i in sorted_result:
                    if i != 0:
                        min_result = i
                        tmp.append(max_result - min_result)
                        break
                for i in range(1, len(sorted_result)):
                    if sorted_result[i-1] != 0:
                        tmp.append(sorted_result[i-1] + 12 - sorted_result[i])
                ans.append(min(tmp) + 1)
    else:
        for j in range(m):
            visited[j] += 1
            result.append(frets[string_idx][j])
            f(string_idx+1, result)
            visited[j] -= 1
            result.pop()
            
n, m = map(int, input().split())
strings = input().split()
chords = input().split()
notes = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
frets = [[] for _ in range(n)]
for i in range(n):
    for j in chords:
        frets[i].append((notes[j]-notes[strings[i]]+12)%12)
ans = []
visited = [0 for _ in range(m)]
f(0, [])
print(min(ans))
"""