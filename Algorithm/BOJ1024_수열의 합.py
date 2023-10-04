"""
수열의 합 공식인 
(첫 값) + (끝 값(=첫 값 + 수열의 길이 - 1)) // 2 * (수열의 길이) = N 임을 이용해
이를 정리해서 첫 값을 구하고
첫 값부터 수열의 길이에 해당하는 리스트를 만든 뒤에 합계와 N을 비교하여 답을 출력하도록 하였음
만약 첫 값이 0보다 작거나 수열의 길이가 100을 초과하는 경우는 -1을 출력하도록 하였음
시간을 단축하기 위해 for문 반복의 범위를 min(101, N + 1)로 하였었는데 이는
입력 1 2 출력 0 1 이라는 반례가 존재해 N + 2로 타협하여 수정하였음
"""
N, L = map(int, input().split())

def get_sequence(target, length):
    start = ((target * 2 // length) + 1 - length) // 2
    if start < 0:
        return []
    
    return list(range(start, start + length))

for length in range(L, min(101, N + 2)):
    temp_sequence = get_sequence(N, length)
    if N == sum(temp_sequence):
        print(*temp_sequence)
        break
else:
    print(-1)