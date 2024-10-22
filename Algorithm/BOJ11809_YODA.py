"""
입력을 리스트에 담아 각 자리수를 역순으로 비교하였고
리스트를 join함수로 다시 합친 후에는 빈 값이 없는지 확인하고
빈 값이라면 YODA를 출력하도록 하였음
"""
N = list(input())
M = list(input())
length = min(len(N), len(M))
for i in range(1, length+1):
    if N[-i] > M[-i]:
        M[-i] = ''
    elif N[-i] < M[-i]:
        N[-i] = ''
N = ''.join(N)
M = ''.join(M)
print(int(N) if N else 'YODA')
print(int(M) if M else 'YODA')
