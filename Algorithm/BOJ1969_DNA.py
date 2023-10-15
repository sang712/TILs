"""
조건에 부합하는 s를 주어진 명단에서 찾는 것인줄 알았는데
새롭게 찾아내는 것이어서
각 자리의 DNA 염기를 카운팅해서 가장 작은 염기와
N - 카운팅을 누적하여 결과를 내 출력하였음
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dnas = [input().strip() for _ in range(N)]

s = []
ans = 0
for i in range(M):
    counter = {}
    for dna in dnas:
        counter.setdefault(dna[i], 0)
        counter[dna[i]] += 1
    target_dna, not_hamming_distance = sorted(list(counter.items()), key=lambda x: (-x[1], x[0]))[0]
    s.append(target_dna)
    ans += N - not_hamming_distance

print(''.join(s), ans, sep='\n')