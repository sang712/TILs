"""
손가락 별로 시작점을 지정하고 1번, 5번 손가락을 다쳤으면 8번씩
그 외의 손가락의 경우 4번씩 카운팅하도록 하였으며 짝수와 홀수의 경우를 나누어 따졌음
"""
finger = int(input())
num = int(input())
if finger == 1 or finger == 5:
    cnt = finger - 1
    cnt += num * 8
else:
    cnt = 1
    if num % 2:
        cnt += (num+1) * 4 - finger
    else:
        cnt += (num+1) * 4 - (6-finger)
print(cnt)