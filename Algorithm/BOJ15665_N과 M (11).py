"""
리스트를 리스트에 어펜드하면 얕은 복사가 되어서 변환을 해주어야 하는데
그냥 프린트로 출력하였음
"""
N, M = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))

sequences = []
sequence = []
def make_sequence():
    if len(sequence) == M:
        print(*sequence)
        return
    
    for num in nums:
        sequence.append(num)
        make_sequence()
        sequence.pop()
make_sequence()