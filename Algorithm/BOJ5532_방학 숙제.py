L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

korean = (A + C - 1) // C
math = (B + D - 1) // D
    
print(L -max(korean, math))
