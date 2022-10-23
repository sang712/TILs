'''
원하는 대로 구현하였음, 시뮬레이션 문제
입력받은 차 순서대로 출력을 해야해서 따로 cars라는 리스트를 만들었음
그리고 차를 보낼 수 있다고 바로 보내면 옆 도로에서 차를 체크할 때 해당 차를 파악할 수 없으므로
동시에 보내도록 기록을 했다가 판단이 끝나면 한 번에 보내는 방법을 사용하였음
주어지는 N은 20만인데에 비해 t가 최대 10억이어서 시간을 건너뛰는 부분이 필요하겠다 생각하였음
그렇게해서 skip_cnt 변수를 두고 4번이 카운팅 되면 넘기려고 했는데 
차가 없는 도로는 영원히 카운팅 되지 않아서 해당 변수를 없애고
skip_to 변수만 게속 바꾸다가 이번 시간에 빠져나가는 차가 아무것도 없으면 건너뛰도록 하였음
pop(0)이라서 deque의 필요성을 느끼지는 못 했음
'''
import sys
input = sys.stdin.readline

# 교차로를 2차원 리스트로 정의하고 원소로 들어간 각 리스트를 큐의 형태로 사용할 예정
intersection = [[],[],[],[]] # A, B, C, D

# 교차로에 들어온 차의 정보를 담기
N = int(input())
cars = [-1]*N
for num in range(N):
    time, road = input().split()
    intersection[ord(road)-ord('A')].append((int(time), num))

# 초기 시간 0, 각 큐를 호출하기 쉽게 A, B, C, D에 배당(얕은 복사)
t = 0
A, B, C, D = intersection
# 차가 교차로에 남아있으면 반복문 실행
while A or B or C or D:
    waiting = 0
    skip_to = 1000000001 # 시간초과를 방지하기 위해 뜨는 시간을 스킵하는 변수
    is_pop = [0, 0, 0, 0] # 지나가도 되는지 체크해두는 리스트
    if A:
        if A[0][0] <= t:
            if D and D[0][0] <= t:
                waiting+=1
            else:
                is_pop[0] = 1
        else:
            skip_to = min(skip_to, A[0][0])
    if B:
        if B[0][0] <= t:
            if A and A[0][0] <= t:
                waiting+=1
            else:
                is_pop[1] = 1
        else:
            skip_to = min(skip_to, B[0][0])
    if C:
        if C[0][0] <= t:
            if B and B[0][0] <= t:
                waiting+=1
            else:
                is_pop[2] = 1
        else:
            skip_to = min(skip_to, C[0][0])
    if D:
        if D[0][0] <= t:
            if C and C[0][0] <= t:
                waiting+=1
            else:
                is_pop[3] = 1
        else:
            skip_to = min(skip_to, D[0][0])
    # 빠져 나갈 차를 보내기
    for i in range(4):
        if is_pop[i]:
            _, num = intersection[i].pop(0)
            cars[num] = t
    # 교착상태면 중단하고 뜨는 시간이 생기면 넘기기
    if waiting == 4:
        break
    elif sum(is_pop) == 0 and skip_to < 1000000001:
        t = skip_to
    else:
        t += 1

#출력
for t in cars:
    print(t)