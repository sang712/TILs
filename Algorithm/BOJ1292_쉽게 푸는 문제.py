"""
while문으로 문제에서 요구하는 수열을 만든 뒤에
해당 구간의 합을 구해 출력하였음
"""
A, B = map(int, input().split())

sequence = []
i = 1
while len(sequence) < B:
    sequence.extend([i] * i)
    i += 1
print(sum(sequence[A-1:B]))