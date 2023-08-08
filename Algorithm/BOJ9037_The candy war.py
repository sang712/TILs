"""
우선 구현을 하면서 3개의 함수를 만들었음
하나는 홀수를 체크하는 함수
하나는 모든 사탕의 개수가 같은지 확인하는 함수
나머지 하나는 사탕의 절반을 옆사람에게 동시에 전달하는 함수
그 후에 while문 안에 세개의 함수를 넣어 반복하도록 하였고
play함수가 호출된 경우에만 카운트를 하여 출력하였음
"""
import sys
input = sys.stdin.readline

def odd_check():
    for i in range(N):
        if kids[i] % 2:
            kids[i] += 1
            
def all_same():
    for i in range(1, N):
        if not kids[i - 1] == kids[i]:
            return False
    return True

def play():
    temp = 0
    for i in range(N):
        kids[i], temp = kids[i] // 2 + temp, kids[i] // 2
    kids[0] += temp

for t in range(int(input())):
    N = int(input())
    kids = list(map(int, input().split()))
    candies = 0
    cnt = 0
    while True:
        odd_check()
        
        if all_same():
            break
        else:
            play()
            cnt += 1
    print(cnt)