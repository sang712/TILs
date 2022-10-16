'''
입력에서 \n을 포함하고 있어서 strip()함수를 사용해 잘라 주었고
전체 문자의 길이의 합이 100만을 넘지 않으므로 다음 코드의 반복이 50만이 되지 않으므로
다음과 같이 코드를 작성하였음
'''
import sys
input = sys.stdin.readline
N = int(input())
def check(string):
    length = len(string)
    while True:
        string = string.replace('AA', '')
        string = string.replace('BB', '')
        if length == len(string): break
        length = len(string)
    if string == '':
        return 1
    else:
        return 0
cnt = 0    
for _ in range(N):
    cnt += check(input().strip())
print(cnt)