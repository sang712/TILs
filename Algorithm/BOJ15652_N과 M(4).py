'''
우선 수열을 리스트로 처리하도록 구상하였고
수열의 마지막에 들어갈 숫자를 n이라는 인자로 받는 함수를 재귀 방식으로 구현하였음

수열의 다음 수는 항상 직전 수보다 크거나 같아야 하므로 
for문의 범위를 n부터 N+1로 줌으로써 해결하였음

재귀적으로 함수를 호출한 뒤에는 마지막으로 넣었던 값을 빼고 for문을 마저 돌도록 하였음
'''
N, M = map(int, input().split())

def make_squence(sequence: list[int], n: int) -> None:
    if len(sequence) == M:
        print(*sequence)
        return
    
    for i in range(n, N + 1):
        sequence.append(i)
        make_squence(sequence, i)
        sequence.pop()

make_squence([], 1)
    