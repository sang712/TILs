"""
왼쪽, 오른쪽에서 각각 시작해 최댓값을 판별하면서 넓이를 구하도록 하였음
좌, 우로 확인하므로 연속으로 발견되는 최댓값이 2개 이상이면 중복될 수 있으므로
MAX 값을 넣어 다음 방향 판별에서는 MAX값이 아닐 경우에만 연산하도록 하였음
flag라는 불리언 변수를 넣어 
같은 최댓값이 최초로 발견된다면 flag를 true로 두고 기둥의 넓이만큼 더해주었고
새로운 최댓값을 발견했을 때는 기둥의 넓이를 더한 것을 상쇄시켰고
그렇지 않고 기존의 최댓값이 계속 발견된다면 그냥 그 차이만 더하도록 하였음
그리고 결과에 flag가 false이고 가장 큰 최댓값은 1개이므로 그 1개 분의 기둥의 넓이를 더해주었음
"""
import sys
input = sys.stdin.readline

N = int(input())
cols = [tuple(map(int, input().split())) for _ in range(N)]
cols.sort(key=lambda x: x[0])
MAX = max(list(zip(*cols))[1])
a = 0
max_h = 0
cur_x = 0
flag = False
for col in cols:
    l, h = col
    if max_h < h:
        a += max_h * (l-cur_x)
        if flag:
            flag = False
            a -= max_h
        cur_x = l
        max_h = h
    elif max_h == h:
        a += max_h * (l-cur_x)
        cur_x = l
        if not flag:
            flag = True
            a += max_h
if flag == False:
    a += max_h

max_h = 0
cur_x = 1001
flag = False
for col in cols[::-1]:
    l, h = col
    if max_h < h:
        a += max_h * (cur_x-l)
        if flag:
            flag = False
            a -= max_h
        cur_x = l
        max_h = h
    elif max_h == h and max_h != MAX:
        a += max_h * (cur_x-l)
        cur_x = l
        if not flag:
            flag = True
            a += max_h
print(a)