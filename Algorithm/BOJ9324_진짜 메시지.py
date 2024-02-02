"""
각 문자열 별로 카운터를 따로 둬서 카운터의 값이 3이되면 그 다음 문자를 확인하도록 하였음
"""
import sys
input = sys.stdin.readline

M = int(input())
for _ in range(M):
    message = input().strip()
    counter = {}
    idx = 0
    while idx < len(message):
        s = message[idx]
        counter.setdefault(s, 0)
        counter[s] += 1
        if counter[s] == 3:
            counter[s] = 0
            idx += 1
            if not (idx < len(message) and s == message[idx]):
                print('FAKE')
                break
        idx += 1
    else:
        print('OK')