import sys
input = sys.stdin.readline

N = int(input())

guitar = []
for _ in range(N):
    serial = input().strip()
    cnt = 0
    for digit in serial:
        if digit.isdigit():
            cnt += int(digit)
            
    guitar.append((serial, cnt))

guitar.sort(key=lambda x: (len(x[0]), x[1], x[0]))

print(*[x[0] for x in guitar], sep='\n')