"""
팀명을 어떻게 적을지 몰라 한글로 변수명을 정했음

문제에서 명시하진 않았지만 문제 설명글을 읽어보면 
이겼을 경우는 입력으로 주어지지 않는 것 같아 해당 경우는 제외하고 구현하였음
"""
제미니스 = list(map(int, input().split()))
걸리버스 = list(map(int, input().split()))

이긴적이있나 = False
제미니스_점수 = 0
걸리버스_점수 = 0
for i in range(9):
    제미니스_점수 += 제미니스[i]
    if 제미니스_점수 > 걸리버스_점수:
        print('Yes')
        break
    걸리버스_점수 += 걸리버스[i]
else:
    print('No')