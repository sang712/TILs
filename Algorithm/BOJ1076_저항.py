"""
첫 색이 검 일 경우와
첫 두 색이 모두 검 일 경우를 예외로 처리해야함
"""
resistance_unit = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 
                   'green': 5, 'blue': 6, 'violet': 7, 'grey' :8, 'white': 9}

resistance = []
for i in range(3):
    color = input()
    if i == 2:
        if resistance:
            resistance.append(resistance_unit[color] * '0')
        else:
            resistance.append(0)
    elif color != 'black' or resistance:
        resistance.append(resistance_unit[color])
    
print(*resistance, sep='')