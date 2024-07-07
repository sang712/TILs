"""
set 자료 구조를 이용하여 
춤을 추고 있는 사람과 만난 사람을 저장한 뒤에
그 수를 출력하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
dancing = set(['ChongChong'])
for _ in range(N):
    a, b = input().split()
    if a in dancing:
        dancing.add(b)
    elif b in dancing:
        dancing.add(a)
print(len(dancing))