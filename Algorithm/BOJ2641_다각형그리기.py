"""
거꾸로된 수열을 얻기 쉽게 하기 위해 리스트로 입력을 받고
수열을 거꾸로 하고 값도 1<->3, 2<->4 으로 서로 교환한 뒤에 2배를 하였음
그 후에 입력으로 주어지는 수열이 해당 두 수열에 연속적으로 존재하는지 판단하기 위해 str 자료형으로 변환하였고
포함된다면 정답으로 출력하도록 하였음
"""
import sys
input = sys.stdin.readline

def reverse(sequence):
    for i in range(len(sequence)):
        if sequence[i] == '1':
            sequence[i] = '3'
        elif sequence[i] == '2':
            sequence[i] = '4'
        elif sequence[i] == '3':
            sequence[i] = '1'
        else:
            sequence[i] = '2'
    return sequence

n = int(input())
standard = input().split() * 2
r_standard = standard[::-1]
r_standard = reverse(r_standard)
standard = ''.join(standard)
r_standard = ''.join(r_standard)
k = int(input())
ans = []
for i in range(k):
    sequence = ''.join(input().split())
    if sequence in standard or sequence in r_standard:
        ans.append(' '.join(sequence))
print(len(ans))
print(*ans, sep='\n')