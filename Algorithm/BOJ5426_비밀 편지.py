"""
문자열을 더하는 연산을 하게되면 시간이 오래 소요되므로
각 문자를 리스트에 append()하는 방식으로 저장했다가 출력할 때
''.join()을 이용해 출력하도록 하여 소요되는 시간을 줄였음
"""
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    secret_letter = input()
    length = int(len(secret_letter) ** 0.5)
    letter = [[] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            letter[j].append(secret_letter[i * length + j])
            
    for i in range(length - 1, -1, -1):
        print(''.join(letter[i]), end='')
    print()