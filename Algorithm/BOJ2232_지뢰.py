import sys
input = sys.stdin.readline

N = int(input())
mines = [(int(input()), i) for i in range(N)]
blown = [0] * N
ans = []
for P, i in sorted(mines, key=lambda x: -x[0]):
    if not blown[i]:
        blown[i] = 1
        ans.append(i + 1)
        chain = P
        j = i + 1
        while j < N:
            if mines[j][0] < chain:
                blown[j] = 1
                chain = mines[j][0]
                j += 1
            else:
                break
        
        chain = P
        j = i - 1
        while j >= 0:
            if mines[j][0] < chain:
                blown[j] = 1
                chain = mines[j][0]
                j -= 1
            else:
                break
print(*sorted(ans), sep='\n')