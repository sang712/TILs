import sys
input = sys.stdin.readline

N = int(input())
half = quater = one_third = ans = 0
for _ in range(N):
    piece = input().strip()
    if piece == '1/2':
        half += 1
    elif piece == '1/4':
        quater += 1
    else:
        one_third += 1

if one_third:
    ans += one_third
    quater -= one_third
    
if half:
    ans += (half+1) // 2
    half %= 2
    if half and quater > 0:
        quater -= 2
        
if quater > 0:
    ans += (quater + 3) // 4
    
print(ans)
