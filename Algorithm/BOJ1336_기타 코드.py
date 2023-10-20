"""
예제 4번에서 확인해봐야하는 건 12까지가 아니라 23까지라는 것을 확인함
-> 23까지 돌려서 2배로 반복할 것이 아니라
나온 프렛 수치에서 정렬한 뒤 나란히 있는 것의 차를 구한 뒤에 12를 더하고 12의 나머지를 구하면 됨
다음과 같이 계산하면
[-1] - [0], [0] - [1], ... [K-1] - [K]
첫번째 연산에서 max() - min()을 구할 수 있고 나머지 연산에서는 나란한 것들의 차를 구할 수 있음
원리는 첫번째 연산을 제외하고 두번째 연산부터, 
인덱스 0번 값에 12를 더해서 이걸 최댓값으로 잡고 1번 값을 최솟값으로 잡으면 차를 1개 구할 수 있고
이 상태에서 인덱스 1번 값에 12를 더해서 이걸 최댓값으로 잡고 2번 값을 최솟값으로 잡아 계산하는 과정을 반복

위에서 [-1] - [0]을 해야하는 걸 [0] - [-1] 해서 틀린답을 도출하였음

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
                temp_fret = sorted(list(set(fret)))
                possible_ans = []
                for i in range(len(temp_fret)):
                    possible_ans.append((temp_fret[i-1] - temp_fret[i] + 12) % 12 + 1)
                ans.add(min(possible_ans))
            else:
                ans.add(0)
        return
    
    tune = tunes[tune_idx]
    if tune in cord:
        candidate.append(tune)
        check_cord(tune_idx + 1, candidate, fret)
        candidate.pop()
    
    for press_fret in range(1, 12):
        fretted_tune = (tune + press_fret) % 12
        if fretted_tune in cord:
            candidate.append(fretted_tune)
            fret.append(press_fret)
            check_cord(tune_idx + 1, candidate, fret)
            candidate.pop()
            fret.pop()

check_cord(0, [], [])
print(0 if 0 in ans else min(ans - {0, }))