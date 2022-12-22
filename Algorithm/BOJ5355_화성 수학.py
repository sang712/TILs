import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    mars_math_eq = list(input().split())
    ans = float(mars_math_eq[0])
    for operator in mars_math_eq[1:]:
        if operator == '@':
            ans *= 3
        elif operator == '%':
            ans += 5
        elif operator == '#':
            ans -= 7
        
    print(f'{ans:.2f}')
