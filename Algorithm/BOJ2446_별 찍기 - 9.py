N = int(input())

ans = []
for i in range(N):
    temp = []
    temp.append(' ' * i)
    temp.append('*' * (2*(N - i) - 1))
    ans.append(''.join(temp))
    
for i in range(2, N + 1):
    temp = []
    temp.append(' ' * (N - i))
    temp.append('*' * (2 * i - 1))
    ans.append(''.join(temp))
    
print(*ans, sep='\n')