N = int(input())

cases = set()

for I in range(N+1):
    for V in range(N+1-I):
        for X in range(N+1-I-V):
            L = N - I - V - X
            cases.add(I + 5*V + 10*X + 50*L)
            
print(len(cases))