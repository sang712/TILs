import sys
input = sys.stdin.readline

def hhmmToM(t):
    h, m = t.split(':')
    return int(h) * 60 + int(m)

S, E, Q = input().split()

S = hhmmToM(S); E = hhmmToM(E); Q = hhmmToM(Q)

list = set()
answer = set()
while True:
    try:
        time, nickname = input().split()
        time = hhmmToM(time)
    except:
        break
    # 시간 비교
    if time <= S:
        list.add(nickname)
    elif E <= time <= Q:
        if nickname in list:
            if nickname not in answer:
                answer.add(nickname)

print(len(answer))
# count가 아니라 in을 사용해서 안에 들어있는지 확인을 했고 이렇게 한 결과 시간초과를 막을 수 있었음