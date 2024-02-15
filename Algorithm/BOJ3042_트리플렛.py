"""
CCW(Counter Clock Wise) 알고리즘을 적용하면 쉽게 풀 수 있는 문제
점 세 개가 있고 이 점 세 개를 순서대로 이은 선의 방향을 알고 싶을 경우
외적을 계산한 값이 0이면 직선, 음수이면 시계방향, 양수이면 반시계방향임을 알 수 있음

근데 왜 내가 한 풀이는 틀렸는지 이해가 가지 않음
-> 2칸떨어지고 3칸 떨어지는 경우는 서로가 배수의 관계가 아니기 때문에 답이 되지 않음ㅋ;

CCW 사용하지 않고 그냥 각 두점을 이은 선의 기울기가 같다는 등식의 모든 항을 한 변에
몰아 사용하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().strip()) for _ in range(N)]

alphabet = []
for i in range(N):
    for j in range(N):
        if board[i][j] != '.':
            alphabet.append((i, j))

length = len(alphabet)
ans = 0
for i in range(length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            ar, ac = alphabet[i]
            br, bc = alphabet[j]
            cr, cc = alphabet[k]

            if (ac-bc)*(br-cr) - (ar-br)*(bc-cc) == 0:
                ans += 1
print(ans)