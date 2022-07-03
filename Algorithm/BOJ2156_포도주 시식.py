'''
sys.stdin.readline()을 이용하여 작성하면
460ms 에서 84ms으로 시간을 확 줄일 수 있음
'''
import sys

N = int(sys.stdin.readline())
dp = [0, 0, 0]
for i in range(N):
    wine = int(sys.stdin.readline())
    if i == 0:
        dp = [wine, 0, 0]
        continue
    d0, d1, d2 = dp
    dp = [d2 + wine, d0 + wine, max(d0, d1, d2)]
print(max(dp))