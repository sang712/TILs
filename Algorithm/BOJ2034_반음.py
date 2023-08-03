"""
도레미파솔라시 총 7개의 경우만 판단하면 되므로 시간초과는 걱정 안 해도 되었었음
우선 입력을 모두 받고
2중 for문으로 라시도레미파솔을 돌고 입력 받은 값을 계속 더해주면서 유효한지 판단하였음
그 후에 유효하다면 정답으로 출력하도록 함
"""
import sys
input = sys.stdin.readline

scales = {0: 'C', 2: 'D', 4: 'E', 5: 'F', 7: 'G', 9: 'A', 11: 'B'}
scales_ = [9, 11, 0, 2, 4, 5, 7]

differences = []
N = int(input())
for _ in range(N):
    differences.append(int(input()))

answer = []
for start in scales_:
    end = start
    for diff in differences:
        end = (end + diff) % 12
        if not end in scales:
            break
    else:
        answer.append((scales[start], scales[end]))
        
for ans in answer:
    print(*ans)