"""
학생을 처음 사진틀에 추가할 때 앞에서 N명을 추가할 것이 아니라
중복여부를 확인하면서 처음 나오는 N명을 추가했어야 했음
이 실수로 여러번 틀린답을 제출하였음
"""
N = int(input())
num_students = int(input())

frames = {}
num_voted = 0
for idx, vote in enumerate(map(int, input().split())):
    if num_voted < N:
        if not vote in frames:
            num_voted += 1
            frames[vote] = [1, idx]
        else:
            frames[vote][0] += 1
        continue
    if vote in frames:
        frames[vote][0] += 1
    else:
        end = sorted(frames, key=lambda x: (frames[x][0], frames[x][1]))[0]
        del frames[end]
        frames[vote] = [1, idx]
print(*sorted(frames))